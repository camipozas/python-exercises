'''
Desarrollar el ejercicio “haciendo la vaca”. 
El programa deberá solicitar la cantidad de personas que aportaran dinero para una futura compra. 
Luego de ingresar a cantidad de personas que participaran y cuanto aporto cada uno, 
el programa deberá mostrar un menú con todas las opciones de compra posible:
“1) Papas fritas $1.000”
“2) Pizza $5.000”
“3) Energética $2.000”
“4) Salir”

El programa deberá descontar el monto asociado a cada compra y 
finalizar cuando no quede mas dinero para adquirir algún producto o elijan la opción ”salir”
'''

print("Haciendo la vaca")
dinero = 0
vaca = int(input("Cuanto personas pondrán dinero?: "))
for i in range(0, vaca):
    aporte = int(input(f"aporte n{i+1}: "))
    dinero = dinero + aporte
print(dinero)

while(dinero > 999):
    print("######################################################")
    print("Que desean llevar?")
    print("1) Papas fritas $1.000")
    print("2) Pizza $5.000")
    print("3) Energética $2.000")
    print("4) Salir")
    opcion = int(input("Ingrese su opción (solo números): "))
    if opcion == 1:
        if (dinero-1000 >= 0):
            dinero = dinero - 1000
            print("######################################################")
            print(f"Les quedan ${dinero} pesos")
        else:
            print("######################################################")
            print("no tienes dinero suficiente!")
    elif opcion == 2:
        if (dinero-5000 >= 0):
            dinero = dinero - 5000
            print("######################################################")
            print(f"Les quedan ${dinero} pesos")
        else:
            print("######################################################")
            print("no tienes dinero suficiente!")
    elif opcion == 3:
        if (dinero-2000 >= 0):
            dinero = dinero - 2000
            print("######################################################")
            print(f"Les quedan ${dinero} pesos")
        else:
            print("######################################################")
            print("no tienes dinero suficiente!")
    elif opcion == 4:
        dinero = 0
    else:
        print("opción invalida")
print("Nos vemos!")
