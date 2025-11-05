# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 05/11/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Fes un programa que elimini els duplicats d'una llista.

llista_amb_duplicats = [x for x in input("Introdueix una llista de paraules separades per espais: ").split()]
llista_sense_duplicats = list(set(llista_amb_duplicats))        
print("Llista sense duplicats:", llista_sense_duplicats)    



