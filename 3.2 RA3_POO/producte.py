# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 21/01/2026
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: 

class Producte:
    def __init__(self, nom, preu):
        self.nom = nom
        self.__preu = preu

    def obtenir_preu(self):
        return self.__preu

    def modificar_preu(self, nou_preu):
        if nou_preu > 0:
            self.__preu = nou_preu