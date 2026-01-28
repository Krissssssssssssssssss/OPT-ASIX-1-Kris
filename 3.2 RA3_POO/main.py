from comptebancari import CompteBancari
from estudiant import Estudiant
from termostat import Termostat
from usuari import Usuari
from sensor import Sensor
from producte import Producte
from rellotge import Rellotge
from alumne import Alumne
from joc import Joc
from compte_usuari import CompteUsuari

print("===== 1. Compte Bancari =====")
compte = CompteBancari(100)
compte.ingressar(50)
compte.retirar(30)
print("Saldo actual:", compte.consultar_saldo())

print("\n===== 2. Estudiant =====")
estudiant = Estudiant(7)
print("Nota inicial:", estudiant.llegir_nota())
estudiant.modificar_nota(9)
print("Nota modificada:", estudiant.llegir_nota())
estudiant.modificar_nota(15)  # no vàlida
print("Nota després d'intent invàlid:", estudiant.llegir_nota())

print("\n===== 3. Termòstat =====")
termostat = Termostat()
print("Temperatura inicial:", termostat.temperatura)
termostat.temperatura = 25
print("Temperatura modificada:", termostat.temperatura)
termostat.temperatura = 35  # no vàlida
print("Temperatura després d'intent invàlid:", termostat.temperatura)

print("\n===== 4. Usuari =====")
usuari = Usuari("password123")
print("Verificar 'password123':", usuari.verificar_contrasenya("password123"))
print("Canviar a '1234':", usuari.canviar_contrasenya("1234"))
print("Canviar a 'nova_contrasenya':", usuari.canviar_contrasenya("nova_contrasenya"))
print("Verificar nova contrasenya:", usuari.verificar_contrasenya("nova_contrasenya"))

print("\n===== 5. Sensor =====")
sensor = Sensor(50)
print("Valor inicial:", sensor.valor)
sensor.valor = 80
print("Valor modificat:", sensor.valor)
sensor.valor = 150  # no vàlid
print("Valor després d'intent invàlid:", sensor.valor)

print("\n===== 6. Producte =====")
producte = Producte("Ordinador", 1000)
print("Producte:", producte.nom)
print("Preu inicial:", producte.obtenir_preu())
producte.modificar_preu(1200)
print("Preu modificat:", producte.obtenir_preu())
producte.modificar_preu(-50)  # no vàlid
print("Preu després d'intent invàlid:", producte.obtenir_preu())

print("\n===== 7. Rellotge =====")
rellotge = Rellotge(9)
print("Hora inicial:", rellotge.mostrar_hora())
rellotge.hores = 15
print("Hora modificada:", rellotge.mostrar_hora())
rellotge.hores = 30  # no vàlida
print("Hora després d'intent invàlid:", rellotge.mostrar_hora())

print("\n===== 8. Alumne =====")
alumne = Alumne(18)
print("Edat inicial:", alumne.edat)
alumne.edat = 20
print("Edat modificada:", alumne.edat)
alumne.edat = -5  # no vàlida
print("Edat després d'intent invàlid:", alumne.edat)

print("\n===== 9. Joc =====")
joc = Joc()
print("Puntuació inicial:", joc.puntuacio)
joc.sumar_punts(10)
joc.sumar_punts(5)
print("Puntuació actual:", joc.puntuacio)
joc.reiniciar()
print("Puntuació després de reiniciar:", joc.puntuacio)

print("\n===== 10. Compte Usuari =====")
compte_usuari = CompteUsuari("usuari@example.com")
print("Email inicial:", compte_usuari.email)
compte_usuari.email = "nou@email.com"
print("Email modificat:", compte_usuari.email)
compte_usuari.email = "email_incorrecte"  # no vàlid
print("Email després d'intent invàlid:", compte_usuari.email)


