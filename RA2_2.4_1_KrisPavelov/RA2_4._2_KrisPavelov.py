# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 05/11/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Demana una frase i compta quantes vocals conté.

frase = input("Introdueix una frase: ")
vocals = "aeiouAEIOU"   
comptador = 0   
for lletra in frase:
    if lletra in vocals:
        comptador += 1  
print("El nombre de vocals és:", comptador) 

