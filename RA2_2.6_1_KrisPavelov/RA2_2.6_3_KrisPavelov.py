# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Afegeix una línia nova a un fitxer existent (sortida.txt) sense esborrar el que ja hi ha.

fitxer = open('sortida.txt', 'a')
fitxer.write("Aquesta es una linia afegida.\n")     
fitxer.close()