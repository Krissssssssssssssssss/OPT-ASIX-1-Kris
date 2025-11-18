# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Escriu una funció factorial(n) que calculi el factorial d'un nombre n de forma recursiva. (Pista: factorial de n és n * factorial(n-1), amb factorial(0) = 1.)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) 
# Exemple d'ús
num = int(input("Introdueix un número per calcular el seu factorial: "))    
resultat = factorial(num)
print(f"El factorial de {num} és: {resultat}")  
