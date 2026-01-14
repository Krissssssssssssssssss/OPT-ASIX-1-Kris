# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Crea una classe PersonaAtributs: nom, edat Mètode presentar_se() que imprimeixi “Hola, soc X i tinc Y anys

class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat

    def presentar_se(self):
        print(f"Hola, soc {self.nom} i tinc {self.edat} anys")
