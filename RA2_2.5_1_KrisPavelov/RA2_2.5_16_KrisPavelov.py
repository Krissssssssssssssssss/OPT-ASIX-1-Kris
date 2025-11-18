# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Multiplica una sèrie de nombres Defineix multiplica_tot(*nombres). Crea dues crides: Multiplica 2, 3, 4. Multiplica 5, 10.

def multiplica_tot(*nombres):
    resultat = 1
    for num in nombres:
        resultat *= num
    return resultat 
producte1 = multiplica_tot(2, 3, 4)
print(f"La multiplicació de 2, 3 i 4 és: {producte1}")
producte2 = multiplica_tot(5, 10)
print(f"La multiplicació de 5 i 10 és: {producte2}")    
    