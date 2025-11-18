"""Càlcul senzill de la força gravitatòria utilitzant constants des de valors_constants.py

Aquest script llegeix tres valors de l'usuari (masses i distància) i mostra la força
gravitòria calculada amb la constant `GRAVETAT` definida a `valors_constants.py`.
"""

import valors_constants


def llegir_float(prompt: str) -> float:
    """Llegeix un float de l'usuari i torna'l. Llança ValueError si l'entrada no és numèrica."""
    return float(input(prompt))


def main() -> None:
    try:
        massa1 = llegir_float("Introdueix la massa del primer objecte (kg): ")
        massa2 = llegir_float("Introdueix la massa del segon objecte (kg): ")
        distancia = llegir_float("Introdueix la distància entre els dos objectes (m): ")
    except ValueError:
        print("Entrada no vàlida — si us plau introdueix nombres (p. ex. 12.34).")
        return

    if distancia == 0:
        print("Error: la distància no pot ser zero.")
        return

    G = valors_constants.GRAVETAT
    forca_gravitatoria = (G * massa1 * massa2) / (distancia ** 2)
    print(f"La força gravitatòria entre els dos objectes és: {forca_gravitatoria} N")


if __name__ == '__main__':
    main()
