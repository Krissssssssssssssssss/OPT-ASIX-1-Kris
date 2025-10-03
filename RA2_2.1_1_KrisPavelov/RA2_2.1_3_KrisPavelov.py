# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Fes un programa que et demani tres números i surti per pantalla el número més gran.

num1=int(input("Introdueix el primer número: "))
num2=int(input("Introdueix el segon número: "))     
num3=int(input("Introdueix el tercer número: "))
if num1>=num2 and num1>=num3:
    print("El número més gran és:", num1)   
elif num2>=num1 and num2>=num3:
    print("El número més gran és:", num2)
else:
    print("El número més gran és:", num3)