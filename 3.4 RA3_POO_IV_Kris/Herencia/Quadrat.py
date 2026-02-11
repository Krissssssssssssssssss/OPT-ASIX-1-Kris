from Figura import Figura

class Quadrat(Figura):
    def __init__(self, costat):
        self.costat = costat

    def area(self):
        return self.costat * self.costat
