# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: 3. Calcula àrees de diversos rectangles Defineix area_rectangle(base, altura). Calcula i imprimeix: L'àrea d'un rectangle de 3x4. L'àrea d'un rectangle de 5x10. L'àrea d'un rectangle de 8x2.

def area_rectangle(base, altura):
    return base * altura    
area1 = area_rectangle(3, 4)
area2 = area_rectangle(5, 10)   
area3 = area_rectangle(8, 2)    
print(f"L'àrea del rectangle de 3x4 és: {area1}")
print(f"L'àrea del rectangle de 5x10 és: {area2}")  
print(f"L'àrea del rectangle de 8x2 és: {area3}")   
    