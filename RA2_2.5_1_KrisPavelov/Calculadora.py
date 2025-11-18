# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Crea un mòdul de càlculs Objectiu: Crea un fitxer calculadora.py amb funcions de suma, resta, multiplicació i divisió. Repte: Importa'l des d’un altre fitxer i crida les funcions amb diferents valors.

def suma(a, b):
    return a + b    
def resta(a, b):
    return a - b        
def multiplicacio(a, b):
    return a * b    
def divisio(a, b):          
    if b != 0:
        return a / b
    else:
        return "Error: Divisió per zero no permesa."    
