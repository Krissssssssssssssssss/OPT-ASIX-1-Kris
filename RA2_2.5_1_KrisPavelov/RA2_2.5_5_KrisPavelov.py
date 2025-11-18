# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Escriu una funció saluda_nom(nom="amic") que imprimeixi "Hola, <nom>". Si no passes cap nom, ha de imprimir "Hola, amic". Fes que l'usuair introduiexi el seu nom.

def saluda_nom(nom="amic"):
    print(f"Hola, {nom}!")
nom_usuari = input("Introdueix el teu nom: ")
if nom_usuari.strip() == "":
    saluda_nom()
else:
    saluda_nom(nom_usuari.strip())

