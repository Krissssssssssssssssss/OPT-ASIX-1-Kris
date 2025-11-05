# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 05/11/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Demana una paraula i verifica si és un palíndrom (ex: "anna", "civic", etc.).

paraula = input("Introdueix una paraula: ")
if paraula == paraula[::-1]:
    print(paraula, "és un palíndrom.")  
else:
    print(paraula, "no és un palíndrom.")   
