# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Suposa que tens un fitxer nombres.txt que hauria de contenir un nombre enter per línia. Fes un programa que llegeixi cada línia i la transformi en enter. Si alguna línia no és un enter vàlid, captura l’error i mostra un missatge, però continua amb la resta. Pista: int(...) pot generar ValueError.

fitxer = open('nombres.txt', 'r')
for linia in fitxer:    
    try:
        nombre = int(linia.strip())  
        print("Nombre llegit:", nombre)  
    except ValueError:
        print("Error: La línia no és un enter vàlid:", linia.strip())   
fitxer.close()  
    