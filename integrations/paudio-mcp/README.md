# paudio-mcp v0.1

Read-only MCP bridge between ChatGPT and explicitly configured local Git
working trees.

This prototype lives on an isolated `ai_control` feature branch so the current
GitHub-based workflow remains unchanged until the mechanism is accepted.

## Scope v0.1

Exposed tools:
- `repo_list`
- `repo_status`
- `repo_head`
- `repo_search`
- `repo_read`
- `repo_diff`

Not exposed:
- arbitrary shell,
- file writes,
- build execution,
- commit/push/reset,
- MCU flashing.

## Requirements

- Windows or Linux,
- Python 3.11+,
- Git available on PATH,
- official MCP Python SDK v2.

Install:

```powershell
cd integrations/paudio-mcp
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
Copy-Item config.example.toml config.toml
```

Edit `config.toml` and point each project id at the correct local checkout.

The server never accepts an arbitrary root path from the model. The model can
only use project ids present in this local config.

## Local validation

Run unit tests:

```powershell
pytest
```

Run MCP Inspector:

```powershell
$env:PAUDIO_MCP_CONFIG = (Resolve-Path .\config.toml)
mcp dev src/paudio_mcp/server.py --with-editable .
```

Run locally over stdio:

```powershell
$env:PAUDIO_MCP_CONFIG = (Resolve-Path .\config.toml)
python src/paudio_mcp/server.py
```

For ChatGPT, OpenAI currently requires a remote MCP endpoint. A local/private
server is connected through Secure MCP Tunnel; ChatGPT does not directly connect
to localhost. Configure that only after the local Inspector tests pass.

## Repository identity guard

Optional file in the project root:

```text
.ai-project-id
```

Example:

```text
project=2lg2_avc
repo_id=2lg2_avc
```

Then set:

```toml
require_identity = true
expected_identity = "2lg2_avc"
```

A mismatch blocks all operations for that configured project. This is intended
to prevent exactly the class of error where changes are made in one checkout
while another checkout is built/tested.

Identity files are not required in v0.1 so the mechanism can be tested without
modifying project repositories.

## Rollback

Nothing in project repositories depends on this MCP server.

To return to the current workflow:
1. set/use `ACCESS_BACKEND=GITHUB`,
2. disable the custom MCP app/tunnel,
3. continue using the GitHub connector.

No project-repository migration or history rewrite is required.


## Local generated files

The following files are intentionally local and ignored by Git:

- `.venv/`
- `config.toml`
- `src/*.egg-info/`
- `**/__pycache__/`
- `.pytest_cache/`
- `uv.lock`

This keeps `repo_status` focused on real source changes while preserving the local
MCP configuration outside the repository history.
