"""Mede quanto da área de um print cada cor ocupa, para conferir a regra 60-30-10.

Uso:
    python ferramentas/medir_cores.py print.png [--cores 6]

Requer: pip install pillow
"""
import argparse
import colorsys
import sys

from PIL import Image


def hex_de(rgb):
    return "#%02X%02X%02X" % rgb


def saturacao(rgb):
    r, g, b = (c / 255 for c in rgb)
    return colorsys.rgb_to_hsv(r, g, b)[1]


def distancia(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5


def medir(caminho, n_cores, juntar=40):
    """Quantiza em muitas cores e junta as parecidas (distância RGB < juntar)."""
    img = Image.open(caminho).convert("RGB")
    img.thumbnail((400, 400))  # rápido e suficiente para proporção de área
    quant = img.quantize(colors=32, method=Image.Quantize.FASTOCTREE, kmeans=2)
    paleta = quant.getpalette()
    grupos = []  # [qtd, rgb]
    for qtd, idx in sorted(quant.getcolors(), reverse=True):
        rgb = tuple(paleta[idx * 3 : idx * 3 + 3])
        for g in grupos:
            if distancia(g[1], rgb) < juntar:
                g[0] += qtd
                break
        else:
            grupos.append([qtd, rgb])
    grupos.sort(reverse=True)
    total = sum(q for q, _ in grupos)
    return [(q / total * 100, rgb) for q, rgb in grupos[:n_cores]]


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("imagem")
    ap.add_argument("--cores", type=int, default=6, help="quantos grupos de cor mostrar (padrão 6)")
    args = ap.parse_args()

    resultado = medir(args.imagem, args.cores)
    print(f"{'Área':>6}  Cor       Saturação")
    for pct, rgb in resultado:
        barra = "█" * round(pct / 2)
        print(f"{pct:5.1f}%  {hex_de(rgb)}  {saturacao(rgb):4.2f}  {barra}")

    # Leitura da regra: as duas maiores áreas e a cor mais saturada entre as menores
    if len(resultado) >= 3:
        principal, secundaria = resultado[0], resultado[1]
        resto = resultado[2:]
        destaque = max(resto, key=lambda x: saturacao(x[1]))
        print()
        print(f"Principal  ~{principal[0]:.0f}%  {hex_de(principal[1])}")
        print(f"Secundária ~{secundaria[0]:.0f}%  {hex_de(secundaria[1])}")
        print(f"Destaque   ~{destaque[0]:.0f}%  {hex_de(destaque[1])} (a cor mais saturada fora das duas maiores)")
        if destaque[0] > 20:
            print("Atenção: o destaque passa de 20% da tela; ele deixa de destacar.")
        if saturacao(principal[1]) > 0.6:
            print("Atenção: a cor que ocupa mais área é muito saturada; o destaque virou fundo.")
        if principal[0] < 40:
            print("Atenção: nenhuma cor domina; a tela pode parecer sem base.")


if __name__ == "__main__":
    sys.exit(main())
