# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Demana a l'usuari un número enter i mostra la seva taula de multiplicar del 1 al 10.

input_num = int(input("Introdueix un número enter: "))
contador = 1
while contador <= 10:
    resultat = input_num * contador
    print(f"{input_num} x {contador} = {resultat}")
    contador = contador + 1 
