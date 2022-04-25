'''
Cree 2 listas, una para los nombres de los 4 vendedores que tiene un negocio (llenada internamente con valores) y 
otra para la cantidad de libros vendidos por cada vendedor (llenada con valores ingresados por teclado).
El programa deberá mostrar de forma ordenada cada vendedor y la cantidad de libros vendidos, con el siguiente formato:
“Juan Pérez vendió 5 libros”
Indique además la cantidad total de libros vendidos, considerando a todos los vendedores y el nombre del mejor vendedor.
'''

nombres = ["Juan Perez", "Pedro Moraga", "Ines Salas", "Enrique Silva"]
ventas = []  # Almacenamos las ventas de cada vendedor en un arreglo
for i in range(4):
    ventas.append(int(input(f"Ingrese ventas para {nombres[i]}: ")))

suma = 0
mayor = 0
mejor = ""

for i in range(4):
    print(nombres[i], "vendió", ventas[i], "libros")
    suma = suma + ventas[i]
    if ventas[i] > mayor:
        mayor = ventas[i]
        mejor = nombres[i]
    elif ventas[i] == mayor:
        mayor = ventas[i]
        mejor = mejor + ", " + nombres[i]

print("Total de libros vendidos = ", suma)
print("Mejor vendedor", mejor)
