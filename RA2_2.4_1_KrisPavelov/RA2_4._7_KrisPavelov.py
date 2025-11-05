# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 05/11/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Demana una cadena i compta quantes vegades apareix una lletra concreta.

cadena = input("Introdueix una cadena: ")
lletra_a_comptar = input("Introdueix la lletra que vols comptar: ")
comptador = 0   
for lletra in cadena:
    if lletra == lletra_a_comptar:
        comptador += 1
print(f"La lletra '{lletra_a_comptar}' apareix vegades {comptador} a la cadena.")   


