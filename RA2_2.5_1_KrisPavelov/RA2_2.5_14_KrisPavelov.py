# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca:  Comprova si diferents nombres són parells Defineix es_parell(numero). Per cada número de la llista [1, 2, 3, 4, 5, 6], crida la funció i imprimeix: "El número X és parell: True/False"

def es_parell(numero):
    return numero % 2 == 0  
# Exemple d'ús
numeros = [1, 2, 3, 4, 5, 6]        
for num in numeros:
    print(f"El número {num} és parell: {es_parell(num)}")   



                                