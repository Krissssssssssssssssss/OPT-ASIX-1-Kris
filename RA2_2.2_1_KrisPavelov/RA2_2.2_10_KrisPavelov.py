# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Utilitzar un bucle per imprimir el següent patró d’estrelles

rows = 5
i = 1
while i <= rows:
    j = 0
    while j < i:
        print("*", end="")
        j += 1
    print("")
    i += 1

