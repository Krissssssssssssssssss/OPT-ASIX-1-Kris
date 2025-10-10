# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Demana a l'usuari una frase i compta quantes vocals conté.

input_phrase = input("Introdueix una frase: ")
vowels = "aeiouAEIOU"
vowel_count = 0 
for char in input_phrase:
    if char in vowels:
        vowel_count += 1    
print("Nombre de vocals a la frase:", vowel_count)

