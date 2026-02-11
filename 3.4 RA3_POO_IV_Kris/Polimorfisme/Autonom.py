from Empleat import Empleat

class Autonom(Empleat):
    def __init__(self, nom, hores_treballades, preu_hora):
        super().__init__(nom)
        self.hores_treballades = hores_treballades
        self.preu_hora = preu_hora

    def calcular_sou(self):
        return self.hores_treballades * self.preu_hora
