# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 05/11/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Fes una llista de números i multiplica tots els elements per 2.

llista_numeros = [int(x) for x in input("Introdueix una llista de nombres separats per espais: ").split()]
llista_multiplicada = [num * 2 for num in llista_numeros]
print("Llista amb els nombres multiplicats per 2:", llista_multiplicada)
        