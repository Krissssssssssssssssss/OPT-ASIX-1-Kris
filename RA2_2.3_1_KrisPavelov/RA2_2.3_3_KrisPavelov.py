# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 17/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Utilitzant el range() escriu un programa que mostri la taula de multiplicar d'un número introduït per l'usuari.

n = int(input("Introdueix un nombre enter per veure la seva taula de multiplicar: "))
print("Taula de multiplicar de", n) 
for i in range(1, 11):
    print(n, "x", i, "=", n * i)    


