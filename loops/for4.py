'''Dado un número entero positivo, mostrar su factorial. 
El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número.'''

# A code that asks for a number and calculates the factorial of that number.
numero = int(input("Número: "))
f = 1
if numero != 0:
    for i in range(1, numero+1):
        f = f*i
print("Factorial:", f)

# Opcion a considerar
# A code that asks for a number and calculates the factorial of that number.
num = int(input('Ingrese factorial'))
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    # run loop 5 times
    for i in range(1, num + 1):
        # multiply factorial by current number
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)
