from Llibre import Llibre

class LlibreDigital(Llibre):
    def __init__(self, titol, autor, format_digital):
        super().__init__(titol, autor)
        self.format_digital = format_digital

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Format: {self.format_digital}")
