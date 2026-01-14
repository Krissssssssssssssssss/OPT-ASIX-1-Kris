# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Crea una classe RectangleAtributs: amplada, alçadaMètodes: area() i perimetre()

class Rectangle:
    def __init__(self, amplada, alçada):
        self.amplada = amplada
        self.alçada = alçada

    def area(self):
        area = self.amplada * self.alçada
        print(area)
    def perimetre(self):
        perimetre = 2 * (self.amplada + self.alçada)
        print(perimetre)
