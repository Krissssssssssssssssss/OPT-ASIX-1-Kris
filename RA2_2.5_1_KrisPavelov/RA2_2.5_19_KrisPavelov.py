# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Determina l'estat de diferents edats Defineix estat_persona(edat). Per les edats [12, 25, 70], crida la funció i imprimeix quin estat retorna.

def estat_persona(edat):
    if edat < 18:
        return "menor d'edat"
    elif 18 <= edat < 65:
        return "adult"
    else:
        return "veterà" 
edats = [12, 25, 70]
for edat in edats:
    estat = estat_persona(edat)    
    print(f"Una persona de {edat} anys és: {estat}")    
