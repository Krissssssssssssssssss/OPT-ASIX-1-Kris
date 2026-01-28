# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 21/01/2026
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: 

class Usuari:
    def __init__(self, contrasenya):
        self.__contrasenya = contrasenya

    def canviar_contrasenya(self, nova):
        if len(nova) >= 8:
            self.__contrasenya = nova
            return True
        return False

    def verificar_contrasenya(self, clau):
        return self.__contrasenya == clau