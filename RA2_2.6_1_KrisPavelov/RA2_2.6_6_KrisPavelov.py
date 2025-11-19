# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Fes un programa que intenti llegir un fitxer anomenat dades.txt, però abans comprovi si existeix. Si no existeix, mostra un missatge d’error amigable.

import os   
if os.path.exists('dades.txt'):
    fitxer = open('dades.txt', 'r')
    contingut = fitxer.read()   
    print(contingut)  
    fitxer.close()  
else:
    print("Error: El fitxer dades.txt no existeix.")    
        