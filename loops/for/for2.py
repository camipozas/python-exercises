'''Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. 
La sucesión comienza con los números 0 y 1 y, a partir de éstos, 
cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…'''

# A way to create a list of numbers.
n1 = 0
n2 = 1

# Otra opcion
# n1, n2 = 0, 1
print(n1)
print(n2)

secuencia = int(input('Ingrese numero de la serie: '))

for i in range(secuencia):
    # add last two numbers to get next number
    n3 = n1+n2
    print(n3)
    n1 = n2
    n2 = n3
