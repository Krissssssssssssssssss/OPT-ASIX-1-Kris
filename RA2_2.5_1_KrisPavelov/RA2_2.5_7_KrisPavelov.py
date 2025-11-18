# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Escriu una funció maxim(a, b, c) que retorni el nombre més gran entre els tres.

def maxim(a, b, c):
    return max(a, b, c) 
a = float(input("Introdueix el primer número: "))
b = float(input("Introdueix el segon número: "))    
c = float(input("Introdueix el tercer número: "))    
resultat = maxim(a, b, c)   
print(f"El nombre més gran entre {a}, {b} i {c} és: {resultat}")        