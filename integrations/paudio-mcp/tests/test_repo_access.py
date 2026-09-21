from __future__ import annotations

from pathlib import Path
import subprocess

import pytest

from paudio_mcp.config import ProjectConfig, ServerConfig
from paudio_mcp.repo_access import RepoAccess, RepoAccessError


def git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


@pytest.fixture()
def repo(tmp_path: Path) -> Path:
    root = tmp_path / "repo"
    root.mkdir()
    git(root, "init")
    git(root, "config", "user.email", "test@example.invalid")
    git(root, "config", "user.name", "Test")
    (root / "src").mkdir()
    (root / "src" / "main.c").write_text(
        "int alpha = 1;\nint beta = 2;\n", encoding="utf-8"
    )
    git(root, "add", ".")
    git(root, "commit", "-m", "init")
    return root


def access(root: Path, *, identity: str | None = None, required: bool = False) -> RepoAccess:
    return RepoAccess(
        ServerConfig(
            projects={
                "demo": ProjectConfig(
                    name="demo",
                    path=root,
                    expected_identity=identity,
                    require_identity=required,
                )
            },
            max_read_lines=50,
            max_file_bytes=100000,
            max_output_chars=100000,
        )
    )


def test_status_and_read(repo: Path) -> None:
    api = access(repo)
    status = api.status("demo")
    assert status["dirty"] is False
    assert len(status["head"]) == 40

    result = api.read("demo", "src/main.c", 1, 2)
    assert "1: int alpha = 1;" in result["content"]
    assert "2: int beta = 2;" in result["content"]


def test_search_and_diff(repo: Path) -> None:
    api = access(repo)
    matches = api.search("demo", "beta")
    assert any("src/main.c:2:int beta = 2;" in x for x in matches["matches"])

    (repo / "src" / "main.c").write_text(
        "int alpha = 3;\nint beta = 2;\n", encoding="utf-8"
    )
    diff = api.diff("demo")
    assert "-int alpha = 1;" in diff["diff"]
    assert "+int alpha = 3;" in diff["diff"]


def test_path_escape_is_blocked(repo: Path, tmp_path: Path) -> None:
    outside = tmp_path / "outside.txt"
    outside.write_text("secret", encoding="utf-8")
    api = access(repo)
    with pytest.raises(RepoAccessError):
        api.read("demo", "../outside.txt")


def test_identity_mismatch_blocks_access(repo: Path) -> None:
    (repo / ".ai-project-id").write_text(
        "project=other\nrepo_id=other\n", encoding="utf-8"
    )
    api = access(repo, identity="demo", required=True)
    with pytest.raises(RepoAccessError, match="identity mismatch"):
        api.status("demo")


def test_identity_match_allows_access(repo: Path) -> None:
    (repo / ".ai-project-id").write_text(
        "project=demo\nrepo_id=demo\n", encoding="utf-8"
    )
    api = access(repo, identity="demo", required=True)
    assert api.status("demo")["identity"]["match"] is True
