'''
#   TODO: Imprimir una figura en la consola. 
Haga un programa en Python que entregue por consola la figura de un rectángulo de ancho y 
largo preguntado por consola usando asteriscos (*)
'''

# Preguntamos por el largo y ancho del rectángulo.

largo = int(input("Ingrese el largo del rectángulo: "))
ancho = int(input("Ingrese el ancho del rectángulo: "))

# Ciclamos la impresión del rectángulo.

for i in range(largo):  # Determina el número de filas que se agregan al rectángulo
    for j in range(ancho):  # Determina el número de columnas que se agregan al rectángulo
        print("*", end=" ")  # Imprime los * en las columnas
    print()  # Imprime las filas
