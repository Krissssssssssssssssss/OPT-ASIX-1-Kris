# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Trobar el número màxim d’una llista

numbers = [3, 5, 2, 8, 1, 4]
max_num = numbers[0]        
for num in numbers:
    if num > max_num:
        max_num = num   
print("El número màxim és:", max_num)
