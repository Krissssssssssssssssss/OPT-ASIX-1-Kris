"""Mòdul `Geometria` amb funcions per calcular àrees.

Funcions exposades:
- area_quadrat(costat)
- area_cercle(radi)
- area_rectangle(base, altura)

Aquest mòdul no fa entrada/sortida per si sol; s'ha d'importar en un script que demani les dades a l'usuari.
"""
from math import pi


def area_quadrat(costat):
	"""Retorna l'àrea d'un quadrat donat el costat.

	Paràmetres:
	- costat: nombre (int o float), longitud del costat (>= 0)

	Retorna:
	- float: àrea = costat ** 2
	"""
	return float(costat) * float(costat)


def area_cercle(radi):
	"""Retorna l'àrea d'un cercle donat el radi.

	Paràmetres:
	- radi: nombre (int o float), radi del cercle (>= 0)

	Retorna:
	- float: àrea = pi * radi ** 2
	"""
	return float(radi) * float(radi) * pi


def area_rectangle(base, altura):
	"""Retorna l'àrea d'un rectangle donades la base i l'altura.

	Paràmetres:
	- base: nombre (int o float)
	- altura: nombre (int o float)

	Retorna:
	- float: àrea = base * altura
	"""
	return float(base) * float(altura)

