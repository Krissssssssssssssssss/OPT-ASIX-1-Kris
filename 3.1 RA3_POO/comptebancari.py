# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Crea una classe CompteBancariAtributs: saldoMètodes: ingressar, retirar, veure saldo

class CompteBancari:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def ingressar(self, quantitat):
        self.saldo += quantitat
        print(f"Ingressats {quantitat}. Saldo actual: {self.saldo}")

    def retirar(self, quantitat):
        if quantitat > self.saldo:
            print("Fons insuficients.")
        else:
            self.saldo -= quantitat
            print(f"Retirats {quantitat}. Saldo actual: {self.saldo}")

    def veure_saldo(self):
        return self.saldo