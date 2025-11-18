# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Escriu una funció filtra_parells(llista) que: Rebi una llista de numeros. Retorni una nova llista només amb els nombres parells.

def filtra_parells(llista):
    return [num for num in llista if num % 2 == 0]  
# Exemple d'ús
entrada = input("Introdueix una llista de numeros separats per espais: ")
numeros = [int(x) for x in entrada.split()]
parells = filtra_parells(numeros)
print(f"Nombres parells: {parells}")
