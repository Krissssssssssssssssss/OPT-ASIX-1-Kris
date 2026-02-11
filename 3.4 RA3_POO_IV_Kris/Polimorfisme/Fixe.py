from Empleat import Empleat

class Fixe(Empleat):
    def __init__(self, nom, sou_fixe):
        super().__init__(nom)
        self.sou_fixe = sou_fixe

    def calcular_sou(self):
        return self.sou_fixe
