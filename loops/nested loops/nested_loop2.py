'''
#   TODO: Imprimir los bordes de la figura en la consola. 
En base a las dimensiones del rectángulo entregadas anteriormente, 
dibuje solo el contorno del rectángulo con los asteriscos.
'''

largo = int(input("Ingrese el largo del rectángulo: "))
ancho = int(input("Ingrese el ancho del rectángulo: "))

# Imprimimos los bordes con * y el resto con guiones -

for i in range(0, largo):
    if i == 0:
        for j in range(0, ancho):
            print("*", end=" ")
    elif i != largo-1:
        for j in range(0, ancho):
            if j == 0:
                print("*", end=" ")
            elif j != ancho - 1:
                print("-", end=" ")
            else:
                print("*", end=" ")
    else:
        for j in range(0, ancho):
            print("*", end=" ")
    print()
