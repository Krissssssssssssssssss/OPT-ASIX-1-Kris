# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca:  Ús del mòdul random. Escriu un programa que simuli llençar un dau (1-6) usant el mòdul random. Prova de fer una funció que llenci el dau n vegades i mostri la mitjana.

import random   
def llançar_dau(n):
    suma = 0
    for _ in range(n):
        tirada = random.randint(1, 6)
        suma += tirada
        print(f"Tirada: {tirada}")
    mitjana = suma / n
    return mitjana  
n_vegades = int(input("Quantes vegades vols llençar el dau? "))
mitjana_resultat = llançar_dau(n_vegades)   
print(f"La mitjana de les tirades és: {mitjana_resultat}")  
