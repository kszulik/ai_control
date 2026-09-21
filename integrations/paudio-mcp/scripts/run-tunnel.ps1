param(
    [string]$Profile = "paudio-local"
)

$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $PSScriptRoot
$Config = Join-Path $Root "config.toml"

if (-not (Test-Path $Config)) { throw "Missing config.toml: $Config" }
if (-not $env:CONTROL_PLANE_API_KEY) { throw "CONTROL_PLANE_API_KEY is not set." }
if (-not (Get-Command tunnel-client -ErrorAction SilentlyContinue)) { throw "tunnel-client is not on PATH." }

$env:PAUDIO_MCP_CONFIG = (Resolve-Path $Config).Path

Write-Host "Starting Secure MCP Tunnel profile $Profile ..."
Write-Host "Keep this terminal open while ChatGPT uses paudio-mcp."
tunnel-client run --profile $Profile
exit $LASTEXITCODE
