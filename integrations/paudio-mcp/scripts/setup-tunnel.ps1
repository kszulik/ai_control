param(
    [Parameter(Mandatory = $true)]
    [ValidatePattern('^tunnel_[0-9a-f]{32}$')]
    [string]$TunnelId,

    [string]$Profile = "paudio-local"
)

$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $PSScriptRoot
$Python = Join-Path $Root ".venv\Scripts\python.exe"
$Server = Join-Path $Root "src\paudio_mcp\server.py"
$Config = Join-Path $Root "config.toml"

if (-not (Test-Path $Python)) { throw "Missing venv Python: $Python" }
if (-not (Test-Path $Server)) { throw "Missing MCP server: $Server" }
if (-not (Test-Path $Config)) { throw "Missing config.toml: $Config" }
if (-not $env:CONTROL_PLANE_API_KEY) { throw "CONTROL_PLANE_API_KEY is not set. Use a runtime API key with Tunnels Read + Use." }
if (-not (Get-Command tunnel-client -ErrorAction SilentlyContinue)) { throw "tunnel-client is not on PATH. Download the supported Windows binary from OpenAI Platform Tunnels." }

$env:PAUDIO_MCP_CONFIG = (Resolve-Path $Config).Path
$McpCommand = '"' + $Python + '" "' + $Server + '"'

Write-Host "Config:  $env:PAUDIO_MCP_CONFIG"
Write-Host "Profile: $Profile"
Write-Host "Tunnel:  $TunnelId"

tunnel-client init --sample sample_mcp_stdio_local --profile $Profile --tunnel-id $TunnelId --mcp-command $McpCommand
if ($LASTEXITCODE -ne 0) { throw "tunnel-client init failed with exit code $LASTEXITCODE" }

tunnel-client doctor --profile $Profile --explain
if ($LASTEXITCODE -ne 0) { throw "tunnel-client doctor failed with exit code $LASTEXITCODE" }

Write-Host ""
Write-Host "Tunnel profile is ready."
