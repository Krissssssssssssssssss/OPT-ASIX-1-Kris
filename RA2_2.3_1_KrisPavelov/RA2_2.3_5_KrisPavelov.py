# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 17/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Demana a l'usuari un nombre enter i imprimeix tots els nombres primers des de 2 fins a aquest nombre.​

n = int(input("Introdueix un nombre enter (>= 2): "))
for num in range(2, n + 1): 

    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)  