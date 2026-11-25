---
name: cores-60-30-10
description: Aplica a regra das cores 60-30-10 numa interface. 60% da área numa cor principal (fundo), 30% numa secundária (cards, barras, blocos) e 10% numa cor de destaque reservada para o que deve chamar atenção (botão principal, estado ativo, número-chave). Use quando pedirem /cores-60-30-10, "regra 60 30 10", "paleta", "as cores estão bagunçadas", "o app não tem identidade", "escolher cor de destaque" ou para revisar as cores de um site, app ou dashboard.
---

# /cores-60-30-10

A regra é sobre **área**, não sobre quantidade de cores:

| Papel | Área | Onde vai | Exemplo |
| --- | --- | --- | --- |
| **Principal** | ~60% | Fundo da página, fundo das telas, áreas grandes | Lona de algodão `#EFE9DF` |
| **Secundária** | ~30% | Cards, barra lateral, cabeçalho, blocos de destaque, texto forte | Tinta berinjela `#3A1E3F` |
| **Destaque** | ~10% | Botão principal, estado ativo/selecionado, progresso, o número que importa | Laranja papaia `#FF6420` |

Principal e secundária costumam ser calmas (neutras ou escuras). O destaque é a única cor saturada e funciona **porque é rara**: se aparece em tudo, deixa de apontar para algum lugar.

## Como trabalhar

### 1. Medir o que existe

- Se houver navegador/Playwright, tire prints das telas principais e rode `python ferramentas/medir_cores.py print.png` (no repositório `guilhermeforprojeto/regra-60-30-10`). Ele agrupa as cores por área e mostra a proporção.
- No código, levante as cores: variáveis CSS, tokens do tema (Tailwind, MUI, Chakra, shadcn), `colors.ts`, `Color(...)` no SwiftUI, `ThemeData` no Flutter. Liste cada cor e **onde** ela é usada.

### 2. Escolher os três papéis

- Se o projeto já tem marca, a cor da marca costuma ser o **destaque**, não o fundo.
- Se não tem, proponha 2 ou 3 trios e deixe a pessoa escolher. Para cada trio: nome, hex, onde cada um entra e um motivo de uma linha.
- Os 60% e 30% precisam de contraste entre si para os blocos aparecerem. O destaque precisa contrastar com os **dois**.
- Cores de estado (erro, aviso, sucesso) ficam fora da conta, mas não podem competir com o destaque: use-as só onde o estado existe.

### 3. Transformar em tokens

Nunca espalhe hex pelo código. Crie tokens com o **papel**, não com o nome da cor:

```css
:root {
  --cor-principal: #EFE9DF;        /* 60: fundo */
  --cor-secundaria: #3A1E3F;       /* 30: blocos */
  --cor-destaque: #FF6420;         /* 10: ação e foco */
  --texto-sobre-principal: #3A1E3F;
  --texto-sobre-secundaria: #EFE9DF;
  --texto-sobre-destaque: #1B0E1D; /* confira o contraste */
}
```

Assim, trocar o destaque (laranja → verde) é mudar **uma** linha, como no vídeo de referência.

### 4. Aplicar

- Fundo e superfícies grandes → principal.
- Cards, menus, cabeçalhos, blocos de dados → secundária (ou variações dela).
- Destaque **só** em: ação principal de cada tela (um botão), item ativo/selecionado, progresso, foco, e no máximo um dado-chave. Botões secundários usam a secundária ou contorno.
- Ícones, ilustrações e gráficos seguem os mesmos papéis.

### 5. Conferir

- **Contraste (WCAG):** texto normal ≥ 4.5:1, texto grande e ícones ≥ 3:1. `python ferramentas/contraste.py "#FF6420" "#EFE9DF"`. Se o destaque não passa com texto branco, use texto escuro sobre ele.
- **Proporção:** meça de novo os prints. Não precisa ser exato; o que importa é a ordem (principal > secundária > destaque) e o destaque ficar perto de 5–15%.
- **Teste do borrão:** com o print desfocado, o olho deve ir direto ao destaque.
- **Modo escuro:** os papéis se mantêm; o principal escurece, a secundária vira uma superfície um pouco mais clara, o destaque costuma ficar igual (confira o contraste).

### 6. Relatar

| Papel | Cor | Antes (% da área) | Depois | Onde mudou |
| --- | --- | --- | --- | --- |

E a lista de componentes que perderam ou ganharam o destaque.

## Não faça

- Não pinte o fundo com o destaque.
- Não use o destaque em textos longos ou em mais de uma ação por tela.
- Não troque a cor da marca sem perguntar.
- Não aplique a regra a fotos e imagens de produto: elas contam como conteúdo, não como paleta.
