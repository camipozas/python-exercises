'''
Escribir una función que calcule el módulo de un vector.
'''

#   Opción 1


def sum_square(x, y):
    '''
    Función que recibe dos valores y calcula la suma del primero más el cuadrado del segundo.
    Parámetros:
        x: Es un número real.
        y: Es un número real.
    Devuelve:
        x + y²
    '''
    return x + y ** 2


def module(v):
    '''
    Función que calcula el módulo de un vector.
    Parámetros:
        v: Una tupla de números reales.
    Devuelve:
        El módulo del vector v.
    '''
    from functools import reduce
    return reduce(sum_square, v, 0) ** 0.5


print(module((3, 4)))
print(module((1, 2, 3)))

#   Opción 2


def module(v):
    '''
    Función que calcula el módulo de un vector.
    Parámetros:
        v: Una tupla de números reales.
    Devuelve:
        El módulo del vector v.
    '''
    return sum([x * 2 for x in v]) * 0.5


print(module((3, 4)))
print(module((1, 2, 3)))
