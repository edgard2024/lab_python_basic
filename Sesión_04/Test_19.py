"""String en cadenas"""
"""Requisitos:
    - Crear una función que multiplicará 3 valores
    - La función tendrá un parámetro o que contendrá un valor
    - Mostrar 2 casos donde se ingrese los valores donde uno no afectará
    el valor del parámetro que ya con tiene un valor
    y otro donde si lo estará afectando"""


def multiplicacion(a,b,c=5):
    return a*b*c


print(multiplicacion(a:2, b:3))
print(multiplicacion(a:2, b:3, c:8))