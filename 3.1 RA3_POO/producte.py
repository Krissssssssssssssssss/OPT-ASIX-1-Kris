# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Crea una classe ProducteAtributs: nom, preuMètode: aplicar un descompte (donat com a percentatge)

class Producte:
    def __init__(self, nom, preu):
        self.nom = nom
        self.preu = preu

    def aplicar_descompte(self, percentatge):
        descompte = self.preu * (percentatge / 100)
        self.preu -= descompte
        print(f"S'ha aplicat un descompte del {percentatge}% al producte {self.nom}. Nou preu: {self.preu}")