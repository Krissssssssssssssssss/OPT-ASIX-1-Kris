# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Fes un programa que donat un número et digui si és més gran o no que zero.

num=int(input("Introdueix un número: "))
if num>0:
    print("El número és més gran que zero") 
elif num==0:
    print("El número és igual a zero")  
else:
    print("El número és més petit que zero")
