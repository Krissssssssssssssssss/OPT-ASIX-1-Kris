# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Crea un mòdul conversions.py amb funcions: celsius_a_fahrenheit(c), fahrenheit_a_celsius(f) Fes servir el mòdul des d’un script principal per convertir diferents valors.

import Modul_graus

temp = int(input("Introdueix la temperatura en Celsius: "))
temp_f = Modul_graus.celsius_a_fahrenheit(temp)
print(f"{temp} graus Celsius són {temp_f} graus Fahrenheit.")