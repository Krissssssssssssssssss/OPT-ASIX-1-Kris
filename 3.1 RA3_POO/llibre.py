# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: . Crea una classe LlibreAtributs: títol, autor, anyMètode mostrar_info() per imprimir les dades

class Llibre:
    def __init__(self, titol, autor, any):
        self.titol = titol
        self.autor = autor
        self.any = any

    def mostrar_info(self):
        print(f"Llibre: '{self.titol}' de {self.autor} ({self.any})")
