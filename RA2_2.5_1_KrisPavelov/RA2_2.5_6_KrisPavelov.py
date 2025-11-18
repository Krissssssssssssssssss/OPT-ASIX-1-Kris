# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Escriu una funció multiplica_tot(*nombres) que rebi qualsevol quantitat de nombres i retorni la seva multiplicació.

def multiplica_tot(*nombres):
    resultat = 1
    for num in nombres:
        resultat *= num
    return resultat 
nombres_input = input("Introdueix nombres separats per espais: ")
nombres = [float(num) for num in nombres_input.split()] 
producte = multiplica_tot(*nombres)
print(f"La multiplicació de tots els nombres és: {producte}")   
    