# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Demana a l'usuari un número enter positiu i determina si és un nombre primer o no

input_num = int(input("Introdueix un número enter positiu: "))
if input_num > 1:
    for i in range(2, int(input_num**0.5) + 1):
        if (input_num % i) == 0:
            print(f"{input_num} no és un nombre primer.")
            break
    else:
        print(f"{input_num} és un nombre primer.")
else:
    print(f"{input_num} no és un nombre primer.")
