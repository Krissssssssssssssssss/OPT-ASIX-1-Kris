from Gat import Gat
from Vaca import Vaca
from Cercle import Cercle
from Quadrat import Quadrat
from Triangle import Triangle
from Fixe import Fixe
from Autonom import Autonom
from Email import Email
from SMS import SMS
from WhatsApp import WhatsApp
from Cotxe import Cotxe as CotxeP
from Bicicleta import Bicicleta
from Barca import Barca

def separador(titol):
    print("\n" + "="*20)
    print(titol)
    print("="*20)

# Exercici 1
separador("Exercici 1: Sons d'animals")
def reproduir_soroll(animal):
    print(animal.fer_soroll())

gat = Gat()
vaca = Vaca()
print("Gat:")
reproduir_soroll(gat)
print("Vaca:")
reproduir_soroll(vaca)

# Exercici 2
separador("Exercici 2: Dibuixar figures")
figures = [Cercle(), Quadrat(), Triangle()]
for figura in figures:
    figura.dibuixar()

# Exercici 3
separador("Exercici 3: Empleats i sous")
def mostrar_sous(llista_empleats):
    for empleat in llista_empleats:
        print(f"Sou de {empleat.nom}: {empleat.calcular_sou()}")

empleats = [
    Fixe("Maria", 2000),
    Autonom("Pere", 160, 20),
    Fixe("Laura", 2500)
]
mostrar_sous(empleats)

# Exercici 4
separador("Exercici 4: Missatgeria")
def enviar_missatges(missatgers, missatge):
    for missatger in missatgers:
        missatger.enviar(missatge)

missatgers = [Email(), SMS(), WhatsApp()]
enviar_missatges(missatgers, "Hola món!")

# Exercici 5
separador("Exercici 5: Transport")
def moure_vehicles(vehicles):
    for vehicle in vehicles:
        vehicle.moure()

vehicles = [CotxeP(), Bicicleta(), Barca()]
moure_vehicles(vehicles)
