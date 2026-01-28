# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 21/01/2026
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: 

class Alumne:
    def __init__(self, edat=0):
        self.__edat = edat

    @property
    def edat(self):
        return self.__edat

    @edat.setter
    def edat(self, valor):
        if valor >= 0:
            self.__edat = valor