# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Escriu una funció area_rectangle(base, altura) que retorni l'àrea (base * altura).

def area_rectangle(base, altura):
    return base * altura    
base = float(input("Introdueix la base del rectangle: "))
altura = float(input("Introdueix l'altura del rectangle: "))    
area = area_rectangle(base, altura)
print(f"L'àrea del rectangle és: {area}")
