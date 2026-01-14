# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Crea una classe CercleAtribut: radiMètodes: calcular àrea i perímetre 

import math
class Cercle:
    def __init__(self, radi):
        self.radi = radi

    def calcular_area(self):
        print(math.pi * self.radi ** 2)

    def calcular_perimetre(self):
        print(2 * math.pi * self.radi)  
    

