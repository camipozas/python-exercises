#Pregunta 1

'''The above code is asking the user to input a street name and a speed. Then, it is checking if the street name is "Siempre Viva" 
and if the speed is greater than 70. If both conditions are true, it will print a message and ask the user to input a value for the fine. 
If the fine is not between 250 and 700, it will print a message. If the speed is less than 50, it will print a message. If the speed is between 50 and 70, 
it will print a message and ask the user to input a value for the fine
'''

calle = input("Ingrese el nombre de la calle/avenida: ")
velocidad = int(input("Ingrese la velocidad: "))

if calle == "Siempre Viva":
    if velocidad > 70:
        print(f"Falta gravísima en {calle} al conducir a una velocidad de {velocidad} km/h")
        multa = int(input("Ingrese el valor de la multa, esta debe ser un valor entre $250 y $700: "))
        if multa>700 or multa < 250:
            print("El valor ingresado es erróneo")
    elif velocidad < 50:
        print("Sin infracción")
    else:
        print(f"Falta grave en {calle} al conducir a una velocidad de {velocidad} km/h")
        multa = int(input("Ingrese el valor de la multa, esta debe ser un valor entre $250 y $700: "))
        if multa>200 or multa < 100:
            print("El valor ingresado es erróneo")

elif calle == "Ruta 6":
    if velocidad >= 140:
        print(f"Falta gravísima en {calle} al conducir a una velocidad de {velocidad} km/h")
        multa = int(input("Ingrese el valor de la multa, esta debe ser un valor entre $500 y $1.000: "))
        if multa>1000 or multa < 500:
            print("El valor ingresado es erróneo")
    elif velocidad < 140:
        print("Sin infracción")

elif calle == "Padre Diagonal":
    if velocidad >= 50:
        print(f"Falta grave en {calle} al conducir a una velocidad de {velocidad} km/h")
        multa = int(input("Ingrese el valor de la multa, esta debe ser un valor entre $300 y $400: "))
        if multa > 400 or multa < 300:
            print("El valor ingresado es erróneo")
    elif velocidad < 50:
        print("Sin infracción")


#Pregunta 2
'''
The above code is asking the user to input a pizza size and the number of pizzas. Then, it is checking if the pizza size is "XXL" 
and if the number of pizzas is greater than 0. If both conditions are true, it will print a message and ask the user to input a value for the name of the person. 
If the pizza size is "XL", it will print a message and ask the user to input a value for the name of the person. If the pizza size is "L", 
it will print a message and ask the user to input a value for the name of the person. If the pizza size is "S", 
it will print a message and ask the user to input a value for the name of the person. If the pizza size is not "XXL", "XL", "L" or "S", it will print a message.
'''

tipo_pizza = input("Ingrese el tipo de Pizza (XXL, XL, L o S): ")
cantidad_pizzas = int(input(f"Ingrese el número de pizzas {tipo_pizza}: "))

for i in range(0,cantidad_pizzas):
    if tipo_pizza == "XXL":
        nombre_1 = input("Ingrese nombre 1: ")
        nombre_2 = input("Ingrese nombre 2: ")
        nombre_3 = input("Ingrese nombre 3: ")
        nombre_4 = input("Ingrese nombre 4: ")
        print(f"Pizza {i+1}: {nombre_1}, {nombre_2}, {nombre_3}, {nombre_4}")
    elif tipo_pizza == "XL":
        nombre_1 = input("Ingrese nombre 1: ")
        nombre_2 = input("Ingrese nombre 2: ")
        nombre_3 = input("Ingrese nombre 3: ")
        print(f"Pizza {i+1}: {nombre_1}, {nombre_2}, {nombre_3}")
    elif tipo_pizza == "L":
        nombre_1 = input("Ingrese nombre 1: ")
        nombre_2 = input("Ingrese nombre 2: ")
        print(f"Pizza {i+1}: {nombre_1}, {nombre_2}")
    elif tipo_pizza == "S":
        nombre_1 = input("Ingrese nombre 1: ")
        print(f"Pizza {i+1}: {nombre_1}")
    else:
        print(f"El tamaño de pizza {tipo_pizza} no existe")
        break
        

#Pregunta 3
'''
The above code is asking the user to input a number of colors and a number of sunshades. Then, it is checking if the number of sunshades is less than 10. 
If the condition is true, it will print a message. If the number of sunshades is greater than or equal to 10 and less than or equal to 20, it will print a message. 
If the number of sunshades is greater than 20 and less than 50, it will print a message. If the number of sunshades is greater than or equal to 50, it will print a message. 
Then, it will print the message as many times as the number of colors. Finally, it will print a message depending on the value of the factor.
'''

colores = int(input("Ingrese el número de colores distintos: "))
quitasoles = int(input("Ingrese el número de quitasoles: "))

if quitasoles < 10:
    oracion = "Esto no prendió"
elif quitasoles >= 10 or quitasoles <= 20:
    oracion = "Está prendiendo la cosa"
elif quitasoles > 20 or quitasoles < 50:
    oracion = "Esto se está saliendo de control"
elif quitasoles >= 50:
    oracion = "Ya perdimos el control"

for i in range(0,colores):
    oracion = oracion + "!!!"

factor = quitasoles*colores*4.5+300

print(oracion)
if factor<500:
    print(f"El factor N es {factor}. Se podrá publicidad")
else:
    print(f"El factor N es {factor}. Se podrá limite al aforo")