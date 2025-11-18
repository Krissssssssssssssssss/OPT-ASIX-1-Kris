# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca:  Troba el màxim de trios de nombres Defineix maxim(a, b, c). Troba el màxim de: (3, 7, 5) (10, 2, 8) (1, 1, 1)

def maxim(a, b, c):
    return max(a, b, c) 
triplets = [(3, 7, 5), (10, 2, 8), (1, 1, 1)]
for a, b, c in triplets:
    resultat = maxim(a, b, c)   
    print(f"El nombre més gran entre {a}, {b} i {c} és: {resultat}")    
        