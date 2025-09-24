# Demanar a l'usuari dos números
num1 = float(input("Introdueix el primer número: "))
num2 = float(input("Introdueix el segon número: "))

# Realitzar les operacions bàsiques
suma = num1 + num2
resta = num1 - num2
multiplicacio = num1 * num2

# Comprovar si el segon número és diferent de zero abans de dividir
if num2 != 0:
    divisio = num1 / num2
else:
    divisio = "No es pot dividir entre zero"

# Mostrar els resultats
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicació: {multiplicacio}")
print(f"Divisió: {divisio}")
