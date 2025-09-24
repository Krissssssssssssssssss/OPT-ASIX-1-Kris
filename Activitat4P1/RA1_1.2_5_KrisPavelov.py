IVA = 0.21 #Constant
def calcular_preu_amb_iva(preu): #Funció
    return preu * (1 + IVA) #Funció
preu = float(input("Introdueix el preu del producte: ")) #Lectura de dades de l'usuari
print("El preu amb IVA és:", calcular_preu_amb_iva(preu)) #Sortida de dades a l'usuari)