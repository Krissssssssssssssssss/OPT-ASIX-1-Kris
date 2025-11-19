# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 09/11/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: 
# Especificació de la tasca: Escriu un programa que llegeixi i mostri el contingut de missatge.txt per pantalla.

fitxer = open('missatge.txt', 'r')
contingut = fitxer.read()
print(contingut)    
fitxer.close()
