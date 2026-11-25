# AGENTS.md — regra 60-30-10

Você (IA) recebeu o link deste repositório. O objetivo é organizar as cores da interface do usuário pela regra 60-30-10: **60% da área numa cor principal, 30% numa secundária e 10% num destaque** reservado para o que deve chamar atenção.

Responda no idioma do usuário.

## O que fazer

1. Leia [`skills/cores-60-30-10/SKILL.md`](skills/cores-60-30-10/SKILL.md): é o procedimento completo (medir, escolher papéis, criar tokens, aplicar, conferir, relatar).
2. Pergunte uma vez, se não estiver claro:
   - **revisar e corrigir agora** o projeto aberto, ou
   - **só sugerir paletas** (2 ou 3 trios com hex e onde cada cor entra), ou
   - **instalar a skill** para usar `/cores-60-30-10` depois: `npx skills add guilhermeforprojeto/regra-60-30-10`, ou `bash instalar.sh` / `powershell -ExecutionPolicy Bypass -File instalar.ps1` num clone deste repositório. Peça permissão antes de instalar.
3. Para medir, use as ferramentas deste repositório (precisam de Python e `pip install pillow`):
   - `python ferramentas/medir_cores.py print.png` → área de cada cor e leitura da regra
   - `python ferramentas/contraste.py "#FF6420" "#EFE9DF"` → contraste WCAG
4. Antes de editar, confira se o projeto está no git com as mudanças salvas. Se não estiver, avise.
5. Entregue a tabela do passo "Relatar" do SKILL.md e, se puder, prints antes e depois medidos pela ferramenta.

## Regras

- Não troque a cor da marca sem perguntar; normalmente ela vira o destaque.
- Destaque só na ação principal de cada tela, no estado ativo, no progresso e em no máximo um dado-chave.
- Todo texto precisa passar no contraste (4.5:1, ou 3:1 para texto grande e ícones).
- Cores em tokens com nome de papel (`--cor-destaque`), nunca hex solto.
- Mude só cores. Layout, espaçamento e tipografia ficam como estão, a menos que a pessoa peça.
