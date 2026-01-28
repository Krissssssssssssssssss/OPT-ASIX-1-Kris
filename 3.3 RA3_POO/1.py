

from abc import ABC, abstractmethod


# =========================
# Interfície Impressora
# =========================
class Impressora(ABC):
    @abstractmethod
    def imprimir(self, contingut):
        pass


# =========================
# Implementacions concretes
# =========================
class ImpressoraPDF(Impressora):
    def imprimir(self, contingut):
        print(f"Imprimint PDF: {contingut}")


class ImpressoraPantalla(Impressora):
    def imprimir(self, contingut):
        print(f"Mostrant per pantalla: {contingut}")


# =========================
# Classe Factura (baix acoblament)
# =========================
class Factura:
    def __init__(self, client, import_total, impressora: Impressora):
        self.client = client
        self.import_total = import_total
        self.impressora = impressora  # Dependència injectada

    def imprimir_factura(self):
        contingut = f"Factura per a {self.client}, total: {self.import_total} €"
        self.impressora.imprimir(contingut)


# =========================
# Exemple d'ús
# =========================
if __name__ == "__main__":
    # Impressió en PDF
    impressora_pdf = ImpressoraPDF()
    factura1 = Factura("Joan", 150, impressora_pdf)
    factura1.imprimir_factura()

    # Impressió per pantalla (sense modificar Factura)
    impressora_pantalla = ImpressoraPantalla()
    factura2 = Factura("Anna", 230, impressora_pantalla)
    factura2.imprimir_factura()