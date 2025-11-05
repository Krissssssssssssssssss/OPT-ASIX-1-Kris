# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 05/11/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Escriu una funció que elimini tots els espais d'una cadena.

def eliminar_espais(cadena):
    return cadena.replace(" ", "")  
cadena_entrada = input("Introdueix una cadena: ")
cadena_sense_espais = eliminar_espais(cadena_entrada)   
print("Cadena sense espais:", cadena_sense_espais)
