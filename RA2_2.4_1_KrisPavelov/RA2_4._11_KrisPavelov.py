# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 05/11/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Crea una llista amb 5 nombres i imprimeix el major i el menor, la llista demana-la tu mateix.

nombres = []
for i in range(5):
    nombre = float(input(f"Introdueix el nombre {i+1}: "))
    nombres.append(nombre)  
major = max(nombres)
menor = min(nombres)    
print("El nombre major és:", major)
print("El nombre menor és:", menor) 

