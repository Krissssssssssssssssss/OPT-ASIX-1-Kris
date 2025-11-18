# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Calcula factorials de diversos nombres Defineix factorial(n). Calcula el factorial de: 0,3,5

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) 
numeros = [0, 3, 5]
for num in numeros: 
    resultat = factorial(num)
    print(f"El factorial de {num} és: {resultat}")      





                        