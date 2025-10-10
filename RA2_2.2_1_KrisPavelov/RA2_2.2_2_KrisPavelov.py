# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Calcula la suma dels primers 100 nombres enters positius (de 1 a 100) i mostra el resultat.

resultat = 0
contador = 0
num = 101
while contador < num:
    resultat = resultat + contador
    contador = contador + 1
    print(resultat)
print("La suma dels primers 100 nombres enters positius és:", resultat)
