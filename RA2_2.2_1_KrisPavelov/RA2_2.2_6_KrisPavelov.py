# Administració de Sistemes Informàtics en Xarxa
#
# Autor: Kris Pavelov
# Data: 03/10/2025
# Descripció: Plantilla per a scripts en bash
# Especificació de la tasca: Mostra els primers 10 termes de la seqüència de Fibonacci.

num_terms = 10
n1, n2 = 0, 1

if num_terms <= 0:
    print("Si us plau, introdueix un nombre enter positiu")
else:
    print("Seqüència de Fibonacci:")
    # Utilitzem num_terms com a control i el decrementem a cada iteració
    # Així evitem un comptador explícit (count) i no fem servir range
    while num_terms:
        print(n1)
        n1, n2 = n2, n1 + n2
        num_terms -= 1

