'''
Crear un programa que permita al usuario ingresar los montos de las compras de un cliente 
(se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), 
cortando el ingreso de datos cuando el usuario ingrese el monto 0.
Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. 
Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, 
se le debe aplicar un 10% de descuento.
'''

total = 0
monto = float(input("Monto de una venta: $"))
while monto != 0:
    if monto < 0:
        print("Monto no válido.")
    else:
        total += monto
    monto = float(input("Monto de una venta: $"))
if total > 1000:
    total -= total*0.1
print("Monto total a pagar: $", total)
