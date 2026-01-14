# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Crea una classe AnimalAtributs: nom, espècieMètode fer_soroll() que mostri un text genèric (“fa un soroll”)

class Animal:
    def __init__(self, nom, especie):
        self.nom = nom
        self.especie = especie

    def fer_soroll(self):
        print("Fa un soroll")
