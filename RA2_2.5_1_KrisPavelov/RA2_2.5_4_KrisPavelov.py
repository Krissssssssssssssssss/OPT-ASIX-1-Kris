# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Escriu una funció es_parell(numero) que retorni True si numero és parell i False si no.

def es_parell(numero):
    return numero % 2 == 0  
# Exemple d'ús
num = int(input("Introdueix un número: "))  
if es_parell(num):  
    print(f"{num} és parell.")  
else:  
    print(f"{num} és senar.")   

            