# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 05/11/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Demana una llista de paraules i crea una nova llista amb només les paraules que comencen per vocal.

paraules = input("Introdueix una llista de paraules separades per espais: ").split()
vocals = 'aeiouAEIOU'   
paraules_amb_vocal = [paraula for paraula in paraules if paraula[0] in vocals]
print("Paraules que comencen per vocal:", paraules_amb_vocal)       
                    