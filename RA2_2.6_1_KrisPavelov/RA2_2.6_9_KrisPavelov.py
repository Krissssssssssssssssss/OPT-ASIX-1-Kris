# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Intenta obrir un fitxer en mode lectura. Si no existeix, crea’l automàticament i escriu-hi una línia per defecte: "Fitxer creat automàticament". Pista: utilitza try-except amb open(...) en mode "r", i si falla, obre'l en mode "w".

try:
    fitxer = open('automagic.txt', 'r')
    contingut = fitxer.read()
    print(contingut)
    fitxer.close()  
except FileNotFoundError:
    fitxer = open('automagic.txt', 'w')
    fitxer.write("Fitxer creat automaticament.\n")  
    fitxer.close()  
    print("El fitxer no existia i ha estat creat automàticament.")  

