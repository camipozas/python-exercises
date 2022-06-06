'''
Requerir al usuario que ingrese un número entero e informar si es primo o no, 
utilizando una función booleana que lo decida.
'''


def primo(num):
    """
    It returns True if the number is prime, and False otherwise

    :param num: The number to be checked
    :return: True or False
    """
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


numero = int(input("Número: "))
if primo(numero):
    print("Es primo")
else:
    print("No es primo")
