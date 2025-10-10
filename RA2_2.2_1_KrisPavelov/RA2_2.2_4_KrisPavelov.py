# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Genera un número aleatori entre 1 i 100. Demana a l'usuari que endevini el número, donant pistes de "massa alt" o "massa baix" fins que l'encerti.

import random
numero_aleatori = random.randint(1, 100)
intents = 0    
endevina = -1
while endevina != numero_aleatori:
    endevina = int(input("Introdueix un número entre 1 i 100: "))
    intents = intents + 1
    if endevina < numero_aleatori:
        print("Massa baix!")
    elif endevina > numero_aleatori:
        print("Massa alt!")
    else:
        print(f"Enhorabona! Has encertat el número {numero_aleatori} en {intents} intents.")
        break

print("Fi del joc.")
