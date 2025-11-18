# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Escriu una funció suma(a, b) que retorni la suma de a i b. Demana els numeros a l'usuari i mostra el resultat.

def suma(a, b):
    return a + b    
a = float(input("Introdueix el primer número: "))
b = float(input("Introdueix el segon número: "))    
resultat = suma(a, b)
print(f"La suma de {a} i {b} és: {resultat}")   

