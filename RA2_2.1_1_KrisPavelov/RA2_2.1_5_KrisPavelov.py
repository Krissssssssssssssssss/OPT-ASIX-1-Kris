# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Fes un programa el qual donada la data de naixement et calculi la edat i et digui si ets o no major d’edat.

from datetime import date
any_naixement=int(input("Introdueix el teu any de naixement: "))
any_actual=date.today().year
edat=any_actual-any_naixement
if edat>=18:
    print("Ets major d'edat, tens", edat, "anys")   
else:
    print("Ets menor d'edat, tens", edat, "anys")
