# Instala a skill /cores-60-30-10 no Claude Code (para todos os projetos).
# Uso: powershell -ExecutionPolicy Bypass -File instalar.ps1            -> %USERPROFILE%\.claude\skills\cores-60-30-10
#      powershell -ExecutionPolicy Bypass -File instalar.ps1 -Projeto   -> .\.claude\skills\cores-60-30-10
param([switch]$Projeto)
$ErrorActionPreference = "Stop"

$origem = Join-Path $PSScriptRoot "skills\cores-60-30-10\SKILL.md"
if (-not (Test-Path $origem)) { Write-Host "Nao achei skills\cores-60-30-10\SKILL.md. Rode a partir do repositorio clonado."; exit 1 }

if ($Projeto) { $destino = Join-Path (Get-Location) ".claude\skills\cores-60-30-10" }
else { $destino = Join-Path $env:USERPROFILE ".claude\skills\cores-60-30-10" }

New-Item -ItemType Directory -Force -Path $destino | Out-Null
Copy-Item $origem (Join-Path $destino "SKILL.md") -Force
Write-Host "Skill instalada em $destino"
Write-Host "Abra o Claude Code no seu projeto e digite: /cores-60-30-10"
