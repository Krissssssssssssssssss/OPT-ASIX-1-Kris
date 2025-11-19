# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Escriu un programa que intenti escriure en un fitxer anomenat resultats.txt, però gestiona l'error que es pot produir si el fitxer és només de lectura o si el sistema impedeix escriure-hi (permisos denegats). Pista: captura PermissionError.

try:
    fitxer = open('resultats.txt', 'w')
    fitxer.write("Aquest es un text de prova.\n")  
    fitxer.close()  
    print("Escriptura al fitxer realitzada amb èxit.")  
except PermissionError:
    print("Error: No tens permisos per escriure en el fitxer resultats.txt.")   
except Exception as e:
    print("S'ha produït un error inesperat:", e)    

    
