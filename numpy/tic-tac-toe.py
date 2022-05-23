import numpy as np

gato = np.zeros([3, 3])
jugadas = 0
while (jugadas < 9):
    # jugada Jugador 1
    jugadas += 1
    for i in range(0, len(gato)):
        for j in range(0, len(gato[i])):
            print(gato[i][j], end=" ")
        print("")

    jug1i = int(input("Jugador 1: Ingresa la coordenada i de tu jugada: "))
    jug1j = int(input("Jugador 1: Ingresa la coordenada j de tu jugada: "))

    while (gato[jug1i][jug1j] != 0):
        print(
            f"Error! en la posición ({jug1i},{jug1j}) ya hay una jugada ingresa otra jugada diferente")
        jug1i = int(input("Jugador 1: Ingresa la coordenada i de tu jugada: "))
        jug1j = int(input("Jugador 1: Ingresa la coordenada j de tu jugada: "))

    gato[jug1i][jug1j] = 1

    # Revisar que el jugador 1 ganó
    ganador1 = False
    # Revisión de filas
    for n in range(0, len(gato)):
        if(gato[n][0] == 1 and gato[n][1] == 1 and gato[n][2] == 1):
            ganador1 = True

        # Revisión de columnas
    for m in range(0, len(gato)):
        if(gato[0][m] == 1 and gato[1][m] == 1 and gato[2][m] == 1):
            ganador1 = True

        # Revisión diagonal principal
    if(gato[0][0] == 1 and gato[1][1] == 1 and gato[2][2] == 1):
        ganador1 = True

        # Revisión diagonal invertida
    if(gato[0][2] == 1 and gato[1][1] == 1 and gato[2][0] == 1):
        ganador1 = True

    if (ganador1 == True and empate == False):
        print("Gana el jugador 1")
        break

    if(jugadas == 9):
        break

    # jugada Jugador 2
    for i in range(0, len(gato)):
        for j in range(0, len(gato[i])):
            print(gato[i][j], end=" ")
        print("")

    jugadas += 1
    jug2i = int(input("Jugador 2: Ingresa la coordenada i de tu jugada: "))
    jug2j = int(input("Jugador 2: Ingresa la coordenada j de tu jugada: "))

    while (gato[jug2i][jug2j] != 0):
        print(
            f"Error! en la posición ({jug2i},{jug2j}) ya hay una jugada ingresa otra jugada diferente")
        jug1i = int(input("Jugador 2: Ingresa la coordenada i de tu jugada: "))
        jug1j = int(input("Jugador 2: Ingresa la coordenada j de tu jugada: "))

    gato[jug2i][jug2j] = 2

    # Revisar que el jugador 2 ganó
    ganador2 = False
    # Revisión de filas
    for n in range(0, len(gato)):
        if(gato[n][0] == 2 and gato[n][1] == 2 and gato[n][2] == 2):
            ganador2 = True

        # Revisión de columnas
    for m in range(0, len(gato)):
        if(gato[0][m] == 2 and gato[1][m] == 2 and gato[2][m] == 2):
            ganador2 = True

        # Revisión diagonal principal
    if(gato[0][0] == 2 and gato[1][1] == 2 and gato[2][2] == 2):
        ganador2 = True

        # Revisión diagonal invertida
    if(gato[0][2] == 2 and gato[1][1] == 2 and gato[2][0] == 2):
        ganador2 = True

    if (ganador2 == True):
        print("Gana el jugador 2")
        break

empate = False
if (ganador1 == False and ganador2 == False):
    print("EMPATE!!!!")


for i in range(0, len(gato)):
    for j in range(0, len(gato[i])):
        print(gato[i][j], end=" ")
    print("")
