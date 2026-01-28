
from abc import ABC, abstractmethod

# Estratègia de descompte

class EstrategiaDescompte(ABC):
    @abstractmethod
    def aplicar(self, total):
        pass

# Implementació concreta

class Descompte20(EstrategiaDescompte):
    def aplicar(self, total):
        return total * 0.8  # 20% de descompte

# Classe CarretCompra

class CarretCompra:
    def __init__(self, total, descompte: EstrategiaDescompte):
        self.total = total
        self.descompte = descompte  # Estratègia injectada

    def calcular_total(self):
        return self.descompte.aplicar(self.total)

# Exemple d'ús

if __name__ == "__main__":
    descompte20 = Descompte20()
    carret = CarretCompra(100, descompte20)

    print(f"Total amb descompte: {carret.calcular_total()} €")