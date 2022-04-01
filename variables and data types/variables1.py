'''1. Se necesita hacer el cambio de pesos chilenos a dólares, el programa pide al usuario el monto y el valor del dolar y el programa hace la conversión'''

# Ingresar nuestro monto
monto = input('Ingrese el monto en CLP: ')
print('El monto ingresado es:', monto)
# Input() lo guarda como un string

# Ingresar el valor del dólar
dolar = input('Ingrese el valor del dólar hoy: ')
print('El valor del dólar es:', dolar)

# Conversión
conversion = int(monto) / int(dolar)
print('CLP a USD:', conversion)

# Extra
# round(numero o variable,cant a redondear)
conversion_round = round(conversion, 2)
print('CLP a USD redondeada:', conversion_round)
