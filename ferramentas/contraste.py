"""Contraste WCAG 2.x entre duas cores.

Uso:
    python ferramentas/contraste.py "#FF6420" "#EFE9DF"
"""
import sys


def luminancia(hex_cor):
    h = hex_cor.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    canais = [int(h[i : i + 2], 16) / 255 for i in (0, 2, 4)]
    lin = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in canais]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]


def contraste(a, b):
    la, lb = sorted((luminancia(a), luminancia(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        return 1
    r = contraste(sys.argv[1], sys.argv[2])
    print(f"Contraste {r:.2f}:1")
    print(f"  Texto normal (AA 4.5):  {'passa' if r >= 4.5 else 'NÃO passa'}")
    print(f"  Texto grande/ícone (3): {'passa' if r >= 3 else 'NÃO passa'}")
    print(f"  Texto normal (AAA 7):   {'passa' if r >= 7 else 'não passa'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
