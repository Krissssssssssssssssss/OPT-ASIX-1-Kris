# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Crida de mòduls amb àlies Crea un mòdul textos.py amb una funció que posi en majúscules, minúscules i capitalitzi textos. Importa’l amb un àlies (import textos as tx) i prova les funcions amb frases diferents.


# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Exemple que crida el mòdul `textos` i mostra transformacions.
# Especificació: importa `textos` amb un àlies i prova les tres funcions.

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

