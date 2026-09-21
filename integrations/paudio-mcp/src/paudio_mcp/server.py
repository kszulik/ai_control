from __future__ import annotations

from mcp.server import MCPServer

from paudio_mcp.config import load_config
from paudio_mcp.repo_access import RepoAccess


mcp = MCPServer(
    "paudio-mcp",
    version="0.1.0",
    instructions=(
        "Read-only access to explicitly configured local Git repositories. "
        "No shell, no writes, no Git mutations."
    ),
)

_access = RepoAccess(load_config())


@mcp.tool()
def repo_list() -> dict[str, object]:
    """List configured local project identifiers."""
    return _access.list_projects()


@mcp.tool()
def repo_status(project: str) -> dict[str, object]:
    """Return local path, branch, HEAD, dirty state, upstream and identity."""
    return _access.status(project)


@mcp.tool()
def repo_head(project: str) -> dict[str, object]:
    """Return compact repository revision metadata."""
    return _access.head(project)


@mcp.tool()
def repo_search(
    project: str,
    query: str,
    path: str | None = None,
    max_results: int = 100,
) -> dict[str, object]:
    """Fixed-string search across tracked files, optionally under a path."""
    return _access.search(project, query, path, max_results)


@mcp.tool()
def repo_read(
    project: str,
    path: str,
    start_line: int = 1,
    end_line: int | None = None,
) -> dict[str, object]:
    """Read a bounded line range from a file inside the configured project."""
    return _access.read(project, path, start_line, end_line)


@mcp.tool()
def repo_diff(project: str, staged: bool = False) -> dict[str, object]:
    """Return the current working-tree or staged Git diff."""
    return _access.diff(project, staged)


if __name__ == "__main__":
    mcp.run()
