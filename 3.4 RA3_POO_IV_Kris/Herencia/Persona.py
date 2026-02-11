class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat

    def saludar(self):
        print(f"Hola, sóc {self.nom}")
