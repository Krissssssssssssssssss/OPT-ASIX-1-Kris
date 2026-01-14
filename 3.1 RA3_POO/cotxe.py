# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca:  Crea una classe Cotxe Atributs: marca, model, any. Mètode per mostrar la informació del cotxe


class Cotxe:
    def __init__(self, marca, model, any):
        self.marca = marca
        self.model = model
        self.any = any

    def mostrar_info(self):
        print(f"Cotxe: {self.marca} {self.model}, Any: {self.any}")