"""Utilities senzilles per transformar textos.

Funcions:
- to_upper(text): retorna `text` en majúscules.
- to_lower(text): retorna `text` en minúscules.
- to_capitalize(text): retorna `text` amb la primera lletra en majúscula i la resta en minúscules.

Les funcions accepten qualsevol objecte convertibile a `str`.
"""

from typing import Any


def to_upper(text: Any) -> str:
	"""Retorna la representació en majúscules de `text`.

	Converteix `text` a `str` i aplica `.upper()`.
	"""
	return str(text).upper()


def to_lower(text: Any) -> str:
	"""Retorna la representació en minúscules de `text`.

	Converteix `text` a `str` i aplica `.lower()`.
	"""
	return str(text).lower()


def to_capitalize(text: Any) -> str:
	"""Retorna `text` amb la primera lletra en majúscula i la resta en minúscules.

	Usa `.capitalize()` després de convertir a `str`.
	Nota: `.capitalize()` posarà en minúscula la resta de caràcters.
	"""
	return str(text).capitalize()

