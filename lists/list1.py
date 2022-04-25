'''
Escriba un programa que almacene 10 números ingresados por teclado en una lista inicialmente vacía.
Determine el promedio de los números pares.
Muestre toda la lista e indique el primer y último número almacenado
'''

# Lista inicialmente vacia
numeros = []
# Llenar con datos por teclado
for i in range(10):
    n = int(input("Ingrese número: "))
    numeros.append(n)

print("Numeros en la lista:", numeros)

# Promediar los números pares
suma = 0
par = 0

for num in numeros:
    if num % 2 == 0:
        par = par + 1  # O par +=1
        suma = suma + num

if par == 0:
    print("No se ingresaron pares")
else:
    print("promedio =", suma/par)

# Primer y último número almacenado
print("Primer = ", numeros[0])
print("Último = ", numeros[9])
