# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 05/11/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Demana a l'usuari 5 paraules i emmagatzema-les en una llista.

paraules = []
for i in range(5):
    paraula = input(f"Introdueix la paraula {i+1}: ")
    paraules.append(paraula)        
print("Llista de paraules:", paraules)  
        