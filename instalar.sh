#!/usr/bin/env bash
# Instala a skill /cores-60-30-10 no Claude Code (para todos os projetos).
# Uso: bash instalar.sh            -> ~/.claude/skills/cores-60-30-10
#      bash instalar.sh --projeto  -> ./.claude/skills/cores-60-30-10 (só este projeto)
set -euo pipefail

ORIGEM="$(cd "$(dirname "$0")" && pwd)/skills/cores-60-30-10"
if [[ "${1:-}" == "--projeto" ]]; then
  DESTINO="./.claude/skills/cores-60-30-10"
else
  DESTINO="$HOME/.claude/skills/cores-60-30-10"
fi

[[ -f "$ORIGEM/SKILL.md" ]] || { echo "❌ Não achei skills/cores-60-30-10/SKILL.md. Rode a partir do repositório clonado."; exit 1; }

mkdir -p "$DESTINO"
cp "$ORIGEM/SKILL.md" "$DESTINO/SKILL.md"
echo "✅ Skill instalada em $DESTINO"
echo "   Abra o Claude Code no seu projeto e digite: /cores-60-30-10"
