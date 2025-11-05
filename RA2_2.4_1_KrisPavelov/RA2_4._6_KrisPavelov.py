# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 05/11/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Demana una cadena i mostra la primera i l'última lletra.

cadena = input("Introdueix una cadena: ")
if len(cadena) > 0:
    print("Primera lletra:", cadena[0])
    print("Última lletra:", cadena[-1]) 
else:
    print("La cadena està buida.")  
    