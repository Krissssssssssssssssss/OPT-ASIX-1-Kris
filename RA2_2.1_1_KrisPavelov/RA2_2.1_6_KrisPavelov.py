# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Fes un programa que demani una lletra i et digui si es vocal o consonant.

lletra=input("Introdueix una lletra: ").lower()
if lletra in 'aeiou':
    print("La lletra és una vocal") 
elif lletra.isalpha() and len(lletra)==1:
    print("La lletra és una consonant") 
else:
    print("Entrada invàlida")
