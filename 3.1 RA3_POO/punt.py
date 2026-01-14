# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Crea una classe PuntAtributs: x, yMètode: calcular la distància a un altre punt

import math 
class Punt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calcular_distancia(self, altre_punt):
        dx = self.x - altre_punt.x
        dy = self.y - altre_punt.y
        print(f"La distància entre els punts és: {math.sqrt(dx**2 + dy**2)}")   
