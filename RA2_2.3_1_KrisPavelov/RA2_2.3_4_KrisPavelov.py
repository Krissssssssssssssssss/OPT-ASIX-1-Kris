# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 17/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Demana a l'usuari un nombre enter i imprimeix tots els nombres parells des de 0 fins a aquest nombre.

n = int(input("Introdueix un nombre enter (>= 0): "))
for i in range(0, n + 1, 2):
    print(i)

    