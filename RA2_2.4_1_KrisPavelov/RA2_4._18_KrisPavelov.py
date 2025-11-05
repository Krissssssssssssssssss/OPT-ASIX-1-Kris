# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 05/11/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Escriu una funció que retorni la llista al revés (sense reverse()).
def revertir_llista(llista):
    return llista[::-1] 
llista_entrada = [x for x in input("Introdueix una llista de nombres separats per espais: ").split()]  
llista_revertida = revertir_llista(llista_entrada)  
print("Llista revertida:", llista_revertida)    
