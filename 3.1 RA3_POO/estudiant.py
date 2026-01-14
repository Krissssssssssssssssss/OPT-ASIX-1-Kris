# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Crea una classe EstudiantAtributs: nom, notaMètode: dir si ha aprovat o no (nota ≥ 5)

class Estudiant:
    def __init__(self, nom, nota):
        self.nom = nom
        self.nota = nota

    def ha_aprovat(self):
        if self.nota >= 5:
            print(f"L'estudiant {self.nom} ha aprovat.")
        else:
            print(f"L'estudiant {self.nom} ha suspès.")
            