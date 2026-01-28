# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 21/01/2026
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: 

class Joc:
    def __init__(self):
        self.__puntuacio = 0

    def sumar_punts(self, punts):
        if punts > 0:
            self.__puntuacio += punts

    def reiniciar(self):
        self.__puntuacio = 0

    @property
    def puntuacio(self):
        return self.__puntuacio