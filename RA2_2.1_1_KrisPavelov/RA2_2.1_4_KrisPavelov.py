# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Fes un programa que et demani un número de l’1 al 10 i segons la nota et digui: “Aprovat” o “Suspès”.

num=int(input("Introdueix un número de l'1 al 10: "))
if num>=5 and num<=10:
    print("Aprovat")    
elif num>=0 and num<5:
    print("Suspès")
else:
    print("Número invàlid")