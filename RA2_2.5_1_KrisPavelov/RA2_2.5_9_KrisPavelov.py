# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Escriu una funció estat_persona(edat) que: Retorni "Menor d'edat", "Adult" o "Jubilat" segons l'edat. Torni tant l'estat com una descripció (return estat, descripcio).

def estat_persona(edat):        
    if edat < 18:
        return "Menor d'edat", "No té dret a votar ni a consumir alcohol."
    elif 18 <= edat < 65:
        return "Adult", "Té dret a votar i a consumir alcohol."
    else:
        return "Jubilat", "Pot gaudir de la seva jubilació."        
edat = int(input("Introdueix la teva edat: "))    
estat, descripcio = estat_persona(edat)     
print(f"Estat: {estat}\nDescripció: {descripcio}")      
