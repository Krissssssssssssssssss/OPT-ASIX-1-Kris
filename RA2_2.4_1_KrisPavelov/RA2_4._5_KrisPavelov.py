# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 05/11/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Substitueix totes les lletres "a" per "@" en una frase donada.

frase = input("Introdueix una frase: ")
frase_modificada = frase.replace("a", "@").replace("A", "@")    
print("Frase modificada:", frase_modificada)
