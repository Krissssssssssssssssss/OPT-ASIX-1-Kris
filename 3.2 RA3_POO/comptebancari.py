# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 21/01/2026
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: 

class CompteBancari:
    def __init__(self, saldo=0):
        self.__saldo = saldo

    def ingressar(self, quantitat):
        if quantitat > 0:
            self.__saldo += quantitat

    def retirar(self, quantitat):
        if 0 < quantitat <= self.__saldo:
            self.__saldo -= quantitat

    def consultar_saldo(self):
        return self.__saldo

