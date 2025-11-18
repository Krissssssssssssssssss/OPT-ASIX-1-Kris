# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Aquest mòdul conté funcions per convertir entre euros i dòlars.

def euros_a_dolars(euros):
    canvi = 1.07   
    return euros * canvi

def dolars_a_euros(dolars):
    canvi = 1.07
    return dolars / canvi

print(euros_a_dolars(50))
print(dolars_a_euros(100))