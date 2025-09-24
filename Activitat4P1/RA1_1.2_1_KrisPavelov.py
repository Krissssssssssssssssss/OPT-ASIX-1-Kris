import math

PI = 3.1416 #Constant

def calcular_area(radi): #fUNCIÓ
    return PI * (radi ** 2) #Funció

radi = float(input("Introdueix el radi: ")) #Lectura de dades de l'usuari
area = calcular_area(radi) #Variable 
print(f"L'àrea del cercle és:", area) #Sortida de dades a l'usuari