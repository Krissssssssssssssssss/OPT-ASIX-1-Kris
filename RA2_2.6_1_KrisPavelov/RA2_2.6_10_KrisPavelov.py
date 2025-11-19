# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Simula una operació amb fitxers on pot haver-hi un error durant la lectura. Assegura’t que el fitxer es tanqui sempre, fins i tot si es produeix un error en llegir-lo. Pista: utilitza try-finally o millor encara: comprova què passa si no utilitzes with i ho fas tot manualment amb .open() i .close().

try:
    fitxer = open('nombres.txt', 'r')
    nombres = fitxer.readlines()
    suma = 0
    for linia in nombres:
        suma += int(linia.strip())
    print("La suma dels nombres és:", suma) 
except Exception as e:
    print("S'ha produït un error durant la lectura del fitxer:", e) 
finally:
    fitxer.close()  
    print("El fitxer s'ha tancat correctament.")    
    
