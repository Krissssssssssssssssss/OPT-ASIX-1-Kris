# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Escriu un mòdul geometria.py amb funcions: area_quadrat(costat) area_cercle(radi) area_rectangle(base, altura) Fes servir-lo per calcular les àrees amb dades introduïdes per l’usuari.

import Geometria    

c = float(input("Introdueix la longitud del costat del quadrat: "))
area_q = Geometria.area_quadrat(c)  
print(f"Àrea del quadrat: {area_q}")    
r = float(input("Introdueix el radi del cercle: "))
area_c = Geometria.area_cercle(r)   
print(f"Àrea del cercle: {area_c}")    
b = float(input("Introdueix la base del rectangle: "))  
h = float(input("Introdueix l'altura del rectangle: "))
area_r = Geometria.area_rectangle(b, h) 