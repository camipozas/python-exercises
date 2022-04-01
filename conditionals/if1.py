''' Se necesita categorizar al usuario dependiendo de la cantidad de puntos acumulados en la tarjeta bancaria "UAISTAR", para ello existen las siguientes categorías:
- Mayor a 5000 puntos: Usuario "Super VIP"
- Mayor a 3500 puntos: Usuario "Golden VIP"
- Mayor a 1500 puntos: Usuario "Golden"
- Mayor a 500 puntos: Usuario "Mechon"
- Menor a 100 puntos: Usuario "¿Quién te conoce?"

El programa deberá solicitar al usuario ingresar la cantidad de puntaje que posee y luego informarle la categoría a la cual pertenece.
'''
# Recordar para correr en shell --> python nombre_archivo.py

# Solicitamos cantidad de puntos
puntos = int(input("Ingrese la cantidad de puntos que tienes: "))

if (puntos > 5000):
    print('Eres usuario Super VIP')
elif (puntos > 3500):
    print('Eres usuario Golden VIP')
elif (puntos > 1500):
    print('Eres usuario Golden')
elif (puntos > 500):
    print('Eres usuario mechón')
else:
    print('Eres usuario quién te conoce')

print('Fin')
