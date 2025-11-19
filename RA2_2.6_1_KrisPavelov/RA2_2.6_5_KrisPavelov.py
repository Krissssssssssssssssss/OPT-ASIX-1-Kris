# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Obre un fitxer en mode lectura i escriptura (r+). Mostra el contingut per pantalla i afegeix una línia al final sense esborrar el contingut anterior.

fitxer = open('sortida.txt', 'r+')
contingut = fitxer.read()   
print(contingut)  
fitxer.write("Aquesta es una linia afegida al final.\n")    
fitxer.close()  
