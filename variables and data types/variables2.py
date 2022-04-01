'''2. Un programa pide la edad de 5 personas, se almacenan en 5 variables (no hemos visto arreglos). El programa entrega el promedio, la suma y la desviación estándar de las edades. Tanto el promedio como la desv. estándar deben ser calculados por su fórmula y no usando las funciones que trae python'''

import numpy

# Ingresamos la edad de 5 personas
edad1 = int(input('Ingrese edad persona 1: '))
edad2 = int(input('Ingrese edad persona 2: '))
edad3 = int(input('Ingrese edad persona 3: '))
edad4 = int(input('Ingrese edad persona 4: '))
edad5 = int(input('Ingrese edad persona 5: '))

# Suma
suma = edad1 + edad2 + edad3 + edad4 + edad5
print('Suma de edades:', suma)

# Promedio
# opcion 1
promedio1 = suma/5
print('Promedio1:', promedio1)

# opcion 2
promedio2 = (edad1 + edad2 + edad3 + edad4 + edad5)/5
print('Promedio2:', promedio2)

# desviación estándar
desv_numerador = (edad1 - promedio1)**2 + (edad2 - promedio1)**2 + (edad3 - promedio1)**2 + (edad4 - promedio1)**2 + (edad5 - promedio1)**2 

desv_estandar = (desv_numerador/5)**(1/2)
print('Desviación estándar: ', desv_estandar)

# No considerar aún ...
edades = [edad1, edad2, edad3, edad4, edad5]
desv = numpy.std(edades)
print(desv)