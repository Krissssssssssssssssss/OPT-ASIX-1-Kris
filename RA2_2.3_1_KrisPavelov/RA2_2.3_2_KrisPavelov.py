# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 17/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Demana a l'usuari un nombre enter i calcula la suma de tots els nombres des de 1 fins a aquest nombre.

n = int(input("Introdueix un nombre enter (>= 1): "))
suma = 0  
for i in range(1, n + 1):
    suma += i 
print("La suma dels nombres des de 1 fins a", n, "és:", suma)

