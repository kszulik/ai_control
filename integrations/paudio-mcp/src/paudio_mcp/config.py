from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os
import tomllib


class ConfigError(RuntimeError):
    pass


@dataclass(frozen=True)
class ProjectConfig:
    name: str
    path: Path
    require_git: bool = True
    identity_file: str = ".ai-project-id"
    expected_identity: str | None = None
    require_identity: bool = False


@dataclass(frozen=True)
class ServerConfig:
    projects: dict[str, ProjectConfig]
    max_read_lines: int = 1000
    max_file_bytes: int = 1_048_576
    max_output_chars: int = 200_000
    git_timeout_seconds: int = 10


def load_config(path: str | os.PathLike[str] | None = None) -> ServerConfig:
    config_path = Path(
        path
        or os.environ.get("PAUDIO_MCP_CONFIG", "")
        or Path.cwd() / "config.toml"
    ).expanduser()

    if not config_path.is_file():
        raise ConfigError(
            f"Config file not found: {config_path}. "
            "Set PAUDIO_MCP_CONFIG or create config.toml."
        )

    with config_path.open("rb") as fh:
        raw = tomllib.load(fh)

    server_raw = raw.get("server", {})
    projects_raw = raw.get("projects", {})
    if not projects_raw:
        raise ConfigError("No projects configured under [projects.*].")

    projects: dict[str, ProjectConfig] = {}
    for name, item in projects_raw.items():
        root = Path(item["path"]).expanduser().resolve()
        projects[name] = ProjectConfig(
            name=name,
            path=root,
            require_git=bool(item.get("require_git", True)),
            identity_file=str(item.get("identity_file", ".ai-project-id")),
            expected_identity=item.get("expected_identity"),
            require_identity=bool(item.get("require_identity", False)),
        )

    return ServerConfig(
        projects=projects,
        max_read_lines=int(server_raw.get("max_read_lines", 1000)),
        max_file_bytes=int(server_raw.get("max_file_bytes", 1_048_576)),
        max_output_chars=int(server_raw.get("max_output_chars", 200_000)),
        git_timeout_seconds=int(server_raw.get("git_timeout_seconds", 10)),
    )
