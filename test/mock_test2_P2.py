#   Pregunta 2
#   Bonificación

nombre = ["Juan", "Claudia", "Catalina"]
nota = [5.6, 4.4, 7.0, 6.8, 5.3, 2.0, 2.0, 4.6, 7, 7, 6, 6]
bonificacion = []

contador = 0
suma = 0
for i in range(len(nombre)):
    #print(f"{nombre[i]} ha obtenido en su evaluacion")
    suma = 0
    for j in range(4):
        # print(nota[contador])
        suma = suma + nota[contador]
        # print(i,contador)
        contador = contador + 1
    #print("promedio ", suma/4)
    promedio = suma/4
    if promedio >= 1 and promedio < 4:
        bonificacion.append(nombre[i])
        bonificacion.append(0)
    elif promedio >= 4 and promedio < 5:
        bonificacion.append(nombre[i])
        bonificacion.append(300000)
    elif promedio >= 5 and promedio < 6.5:
        bonificacion.append(nombre[i])
        bonificacion.append(500000)
    else:
        bonificacion.append(nombre[i])
        bonificacion.append(800000)
print(bonificacion)
