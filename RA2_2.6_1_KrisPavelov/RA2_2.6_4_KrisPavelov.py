# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Llegeix el fitxer (sortida.txt) i mostra quantes línies té.

fitxer = open('sortida.txt', 'r')
linies = fitxer.readlines()     
print("El fitxer té", len(linies), "línies.")
fitxer.close()  