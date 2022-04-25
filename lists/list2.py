'''
Escriba un programa que almacene en una lista el nombre y género (h/m) de 5 personas ingresados por teclado.
A partir de los datos allí almacenados generar 2 listas: una con el nombre de los hombres y otra con las mujeres.
El programa debe mostrar los nombres de los hombres y las mujeres ordenados alfabéticamente y 
determinar si fueron ingresados más hombres o más mujeres. 
Ejemplo:
Ingrese un nombre: Ivan
Ingrese su genero (h/m): h
Ingrese un nombre: Claudia
Ingrese su genero (h/m): m
Ingrese un nombre: Andres
Ingrese su genero (h/m): h
Ingrese un nombre: Horacio
Ingrese su genero (h/m): h
Ingrese un nombre: Ana
Ingrese su genero (h/m): m
Hombres alfabéticamente: ['Andres', 'Horacio', 'Ivan'] Mujeres alfabeticamente: ['Ana', 'Claudia']
Hay más hombres que mujeres
'''

nombres = []
hombres = []
mujeres = []

for i in range(5):
    nombres.append(input("Ingrese un nombre: "))
    nombres.append(input("Ingrese su genero (h/m): "))

for i in range(1, len(nombres), 2):
    if nombres[i] == "h":
        hombres.append(nombres[i-1])
    elif nombres[i] == "m":
        mujeres.append(nombres[i-1])
    hombres.sort()
    mujeres.sort()
print("Hombres alfabeticamente:", hombres)
print("Mujeres alfabeticamente:", mujeres)

if len(hombres) > len(mujeres):
    print("Hay mas hombres que mujeres")
else:
    print("hay mas mujeres que hombres")
