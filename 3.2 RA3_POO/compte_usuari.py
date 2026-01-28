# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 21/01/2026
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: 

class CompteUsuari:
    def __init__(self, email):
        self.__email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, nou_email):
        if "@" in nou_email and "." in nou_email:
            self.__email = nou_email