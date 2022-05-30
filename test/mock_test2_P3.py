#   Ejercicio 3
#   Reserva vuelos

import numpy as np

letras = ["A", 0, "B", 1, "C", 2, "D", 3, "E", 4, "F", 5, "G", 6]
avion = np.zeros((7, 3))

if avion.sum() == 21:
    print("No quedan asientos para este vuelo")

print("Asientos disponibles: ")
for i in range(avion.shape[0]):
    for j in range(avion.shape[1]):
        if avion[i][j] == 0:
            print(letras[i*2]+str(j+1))

print("Disponibles juntos:")
for i in range(avion.shape[0]):
    if avion[i][1] == 0 and avion[i][2] == 0:
        print(f"{letras[i*2]}2-{letras[i*2]}3")

print("Disponibles individuales")
for i in range(avion.shape[0]):
    if avion[i][0] == 0:
        print(f"{letras[i*2]}1")

print("Filas disponibles:")
for i in range(avion.shape[0]):
    # if sum(avion[i,:])==0:
    #   print(f"Disponible Fila {letras[i*2]}")
    if avion[i][0] == 0 and avion[i][1] == 0 and avion[i][2] == 0:
        print(f"Fila {letras[i*2]}")

print(avion)
cantidad = int(input("Ingrese en numero de asientos que desea reservar: "))
while cantidad > 0:
    posicion = []
    asiento = input("Ingrese el asiento que quiere reservar: ")
    posicion.extend(asiento)
    posicion[1] = int(posicion[1])
    if posicion[1] == 1:
        print("El precio de ese asiento es: 125.000 pesos")
        precio = 125000
    elif posicion[1] == 2:
        print("El precio de ese asiento es: 90.000 pesos")
    if posicion[1] == 3:
        print("El precio de ese asiento es: 100.000 pesos")
    opcion = input("Desea confirmar S/N: ")
    if opcion == "S":
        avion[int(letras.index(posicion[0])/2)][int(posicion[1])-1] = 1
        cantidad = cantidad - 1
        print(f"Asiento {asiento} reservado")
    else:
        break
print(avion)


# print(avion)
# print(avion.sum())
# print(avion.shape)
# print(avion.shape[0])
# print(avion.shape[1])
