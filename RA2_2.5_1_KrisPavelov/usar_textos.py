"""Script senzill que utilitza el mòdul `textos` per transformar una frase d'exemple.
"""

import textos as tx


def main():
    frase1 = "Hola Món"
    frase2 = "Hola MÓN"
    frase3 = "hola món"

    print("Original:")
    print("  ", frase1)
    print("  ", frase2)
    print("  ", frase3)

    print("\nTransformacions:")
    print("  Majúscules:", tx.to_upper(frase1))
    print("  Minúscules:", tx.to_lower(frase2))
    print("  Capitalitza:", tx.to_capitalize(frase3))


if __name__ == '__main__':
    main()
