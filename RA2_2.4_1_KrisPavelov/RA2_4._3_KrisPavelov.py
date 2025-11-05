# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 05/11/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Escriu una funció que reverteixi una cadena.

def revertir_cadena(cadena):
    return cadena[::-1]     
cadena_entrada = input("Introdueix una cadena: ")
cadena_revertida = revertir_cadena(cadena_entrada)  
print("Cadena revertida:", cadena_revertida)
