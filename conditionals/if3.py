'''Calculo discriminante'''

a = int(input("Introducir valor de a:"))
b = int(input("introducir valor de b:"))
c = int(input("introducir valor de c:"))
discriminante = b**-4*a*c

if discriminante < 0:
    print("2 soluciones reales y distintas")
elif discriminante == 0:
    print("2 soluciones reales e iguales")
elif discriminante > 0:
    print("soluciones complejas")
