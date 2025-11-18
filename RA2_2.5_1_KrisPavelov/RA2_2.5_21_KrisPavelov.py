import Calculadora

numero1= int (input("Introdueix la primera xifra: "))
numero2= int (input("Introdueix la segona xifra: "))


resultat = Calculadora.suma(numero1, numero2)
print(f"La suma de {numero1} i {numero2} és: {resultat}")

resultat = Calculadora.resta(numero1, numero2)
print(f"La resta de {numero1} i {numero2} és: {resultat}")

resultat = Calculadora.multiplicacio(numero1, numero2)
print(f"La multiplicació de {numero1} i {numero2} és: {resultat}")  

resultat = Calculadora.divisio(numero1, numero2)
print(f"La divisió de {numero1} i {numero2} és: {resultat}")    

