# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 05/11/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Demana 10 números i crea dues llistes: una amb els parells i una altra amb els senars.

parells = []
senars = [] 
for i in range(10):
    numero = int(input(f"Introdueix el número {i+1}: "))
    if numero % 2 == 0:
        parells.append(numero)
    else:
        senars.append(numero)   
print("Llista de números parells:", parells)
print("Llista de números senars:", senars)  



