# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 05/11/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Crea un programa que divideixi una frase en paraules i les mostri una per una.

frase = input("Introdueix una frase: ")
paraules = frase.split()    
for paraula in paraules:
    print(paraula)  

