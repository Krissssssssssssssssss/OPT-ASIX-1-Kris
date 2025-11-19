# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Crea un programa que escrigui les següents 3 línies en un fitxer nou anomenat sortida.txt. El contingut anterior (si n'hi ha) ha de desaparèixer.

fitxer = open('sortida.txt', 'w')
fitxer.write("Primera linia.\n")  
fitxer.write("Segona linia.\n")
fitxer.write("Tercera linia.\n")  
fitxer.close()  
