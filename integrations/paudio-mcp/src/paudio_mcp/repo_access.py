from __future__ import annotations

from dataclasses import asdict
from pathlib import Path
import subprocess

from .config import ProjectConfig, ServerConfig


class RepoAccessError(RuntimeError):
    pass


def _truncate(text: str, limit: int) -> tuple[str, bool]:
    if len(text) <= limit:
        return text, False
    return text[:limit] + "\n...[truncated]...", True


class RepoAccess:
    def __init__(self, config: ServerConfig):
        self.config = config

    def _project(self, name: str) -> ProjectConfig:
        try:
            project = self.config.projects[name]
        except KeyError as exc:
            raise RepoAccessError(f"Unknown project: {name}") from exc

        if not project.path.is_dir():
            raise RepoAccessError(
                f"Configured project directory does not exist: {project.path}"
            )
        if project.require_git and not (project.path / ".git").exists():
            raise RepoAccessError(
                f"Configured project is not a Git working tree: {project.path}"
            )
        self._verify_identity(project)
        return project

    def _verify_identity(self, project: ProjectConfig) -> dict[str, object]:
        identity_path = project.path / project.identity_file
        if not identity_path.is_file():
            if project.require_identity:
                raise RepoAccessError(
                    f"Identity file missing for {project.name}: {identity_path}"
                )
            return {
                "required": project.require_identity,
                "present": False,
                "expected": project.expected_identity,
                "actual": None,
                "match": None,
            }

        values: dict[str, str] = {}
        for line in identity_path.read_text(encoding="utf-8", errors="replace").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            values[key.strip()] = value.strip()

        actual = values.get("repo_id") or values.get("project")
        match = (
            None
            if project.expected_identity is None
            else actual == project.expected_identity
        )
        if project.expected_identity is not None and not match:
            raise RepoAccessError(
                f"Repository identity mismatch for {project.name}: "
                f"expected={project.expected_identity!r}, actual={actual!r}"
            )
        return {
            "required": project.require_identity,
            "present": True,
            "expected": project.expected_identity,
            "actual": actual,
            "match": match,
        }

    def _git(self, project: ProjectConfig, *args: str, allow_fail: bool = False) -> str:
        proc = subprocess.run(
            ["git", "-C", str(project.path), *args],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=self.config.git_timeout_seconds,
            check=False,
        )
        if proc.returncode != 0 and not allow_fail:
            raise RepoAccessError(
                f"git {' '.join(args)} failed ({proc.returncode}): "
                f"{proc.stderr.strip()}"
            )
        return proc.stdout.strip()

    def _safe_file(self, project: ProjectConfig, relative_path: str) -> Path:
        if not relative_path or Path(relative_path).is_absolute():
            raise RepoAccessError("Path must be a non-empty relative path.")

        root = project.path.resolve()
        candidate = (root / relative_path).resolve()
        if candidate != root and root not in candidate.parents:
            raise RepoAccessError("Path escapes configured project root.")
        if not candidate.is_file():
            raise RepoAccessError(f"File not found: {relative_path}")
        if candidate.stat().st_size > self.config.max_file_bytes:
            raise RepoAccessError(
                f"File too large for repo_read: {candidate.stat().st_size} bytes"
            )
        return candidate

    def list_projects(self) -> dict[str, object]:
        return {
            "projects": [
                {
                    "project": name,
                    "configured": True,
                    "require_identity": cfg.require_identity,
                }
                for name, cfg in sorted(self.config.projects.items())
            ]
        }

    def status(self, name: str) -> dict[str, object]:
        project = self._project(name)
        branch = self._git(project, "rev-parse", "--abbrev-ref", "HEAD")
        head = self._git(project, "rev-parse", "HEAD")
        porcelain = self._git(project, "status", "--porcelain=v1")
        upstream = self._git(
            project,
            "rev-parse",
            "--abbrev-ref",
            "--symbolic-full-name",
            "@{upstream}",
            allow_fail=True,
        )
        ahead = behind = None
        if upstream:
            counts = self._git(
                project,
                "rev-list",
                "--left-right",
                "--count",
                f"HEAD...{upstream}",
                allow_fail=True,
            )
            if counts:
                left, right = counts.split()
                ahead = int(left)
                behind = int(right)

        return {
            "project": name,
            "root": str(project.path),
            "branch": branch,
            "head": head,
            "dirty": bool(porcelain),
            "changed_files": porcelain.splitlines()[:200],
            "upstream": upstream or None,
            "ahead": ahead,
            "behind": behind,
            "identity": self._verify_identity(project),
        }

    def head(self, name: str) -> dict[str, object]:
        status = self.status(name)
        return {
            key: status[key]
            for key in (
                "project",
                "root",
                "branch",
                "head",
                "dirty",
                "upstream",
                "ahead",
                "behind",
                "identity",
            )
        }

    def search(
        self,
        name: str,
        query: str,
        path: str | None = None,
        max_results: int = 100,
    ) -> dict[str, object]:
        if not query:
            raise RepoAccessError("Search query must not be empty.")
        if max_results < 1 or max_results > 500:
            raise RepoAccessError("max_results must be in range 1..500.")

        project = self._project(name)
        args = ["grep", "-n", "-I", "-F", "-e", query]
        if path:
            args.extend(["--", path])

        output = self._git(project, *args, allow_fail=True)
        lines = output.splitlines()
        selected = lines[:max_results]
        text, truncated_chars = _truncate(
            "\n".join(selected), self.config.max_output_chars
        )
        return {
            "project": name,
            "query": query,
            "path": path,
            "matches": text.splitlines() if text else [],
            "match_count_returned": len(selected),
            "result_limit_hit": len(lines) > max_results or truncated_chars,
        }

    def read(
        self,
        name: str,
        path: str,
        start_line: int = 1,
        end_line: int | None = None,
    ) -> dict[str, object]:
        project = self._project(name)
        file_path = self._safe_file(project, path)

        if start_line < 1:
            raise RepoAccessError("start_line must be >= 1.")

        lines = file_path.read_text(
            encoding="utf-8", errors="replace"
        ).splitlines()
        if end_line is None:
            end_line = min(len(lines), start_line + self.config.max_read_lines - 1)
        if end_line < start_line:
            raise RepoAccessError("end_line must be >= start_line.")
        if end_line - start_line + 1 > self.config.max_read_lines:
            raise RepoAccessError(
                f"Requested range exceeds max_read_lines={self.config.max_read_lines}."
            )

        selected = lines[start_line - 1 : end_line]
        numbered = [
            f"{line_no}: {line}"
            for line_no, line in enumerate(selected, start=start_line)
        ]
        content, truncated = _truncate(
            "\n".join(numbered), self.config.max_output_chars
        )
        return {
            "project": name,
            "path": path,
            "start_line": start_line,
            "end_line": start_line + len(selected) - 1,
            "total_lines": len(lines),
            "content": content,
            "truncated": truncated,
        }

    def diff(self, name: str, staged: bool = False) -> dict[str, object]:
        project = self._project(name)
        args = ["diff", "--no-ext-diff", "--unified=3"]
        if staged:
            args.append("--cached")
        output = self._git(project, *args)
        content, truncated = _truncate(output, self.config.max_output_chars)
        return {
            "project": name,
            "staged": staged,
            "diff": content,
            "truncated": truncated,
        }
