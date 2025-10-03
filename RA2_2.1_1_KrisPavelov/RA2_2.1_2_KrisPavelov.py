# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Fes un programa que donat un número et digui si és parell o imparell.

num=int(input("Introdueix un número: "))
if num%2==0:
    print("El número és parell")    
else:
    print("El número és imparell")