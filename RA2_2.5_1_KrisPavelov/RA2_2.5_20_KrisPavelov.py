# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Filtra nombres parells de diverses llistes Defineix filtra_parells(llista). Aplica la funció a: [1, 2, 3, 4, 5, 6], [10, 15, 20, 25, 30]

def filtra_parells(llista):
    return [num for num in llista if num % 2 == 0]  
llistes = [[1, 2, 3, 4, 5, 6], [10, 15, 20, 25, 30]]
for llista in llistes:      
    parells = filtra_parells(llista)
    print(f"Nombres parells de {llista}: {parells}")






                                        