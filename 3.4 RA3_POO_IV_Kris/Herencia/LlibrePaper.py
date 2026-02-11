from Llibre import Llibre

class LlibrePaper(Llibre):
    def __init__(self, titol, autor, n_pagines):
        super().__init__(titol, autor)
        self.n_pagines = n_pagines

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Pàgines: {self.n_pagines}")
