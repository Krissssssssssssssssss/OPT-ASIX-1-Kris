# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 05/11/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Escriu una funció que sumi tots els nombres d'una llista.

def sumar_llista(numeros):
    return sum(numeros) 
llista_numeros = [int(x) for x in input("Introdueix una llista de nombres separats per espais: ").split()]  
suma = sumar_llista(llista_numeros)
print("La suma dels nombres és:", suma) 
    