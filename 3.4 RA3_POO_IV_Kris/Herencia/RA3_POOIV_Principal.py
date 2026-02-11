from Gos import Gos
from Gat import Gat
from Cotxe import Cotxe
from Treballador import Treballador
from Quadrat import Quadrat
from Cercle import Cercle
from LlibrePaper import LlibrePaper
from LlibreDigital import LlibreDigital

def separador(titol):
    print("\n" + "="*20)
    print(titol)
    print("="*20)

# Exercici 1
separador("Exercici 1: Animals")
gos = Gos()
gat = Gat()
print("Gos:")
gos.parlar()
print("Gat:")
gat.parlar()

# Exercici 2
separador("Exercici 2: Vehicles")
cotxe = Cotxe("Toyota")
cotxe.arrencar()
cotxe.tocar_claxon()

# Exercici 3
separador("Exercici 3: Persones i treballadors")
treballador = Treballador("Joan", 30, "Programador")
treballador.saludar()
treballador.mostrar_feina()

# Exercici 4
separador("Exercici 4: Figura geomètrica")
quadrat = Quadrat(5)
cercle = Cercle(3)
print(f"Àrea del quadrat (costat 5): {quadrat.area()}")
print(f"Àrea del cercle (radi 3): {cercle.area():.2f}")

# Exercici 5
separador("Exercici 5: Biblioteca")
llibre_paper = LlibrePaper("El Quixot", "Cervantes", 1000)
llibre_digital = LlibreDigital("Python 101", "Guido van Rossum", "PDF")
print("Llibre de paper:")
llibre_paper.mostrar_info()
print("\nLlibre digital:")
llibre_digital.mostrar_info()
