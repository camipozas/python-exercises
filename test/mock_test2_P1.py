#   Pregunta 1
#   Vuelto supermercado

productos = []
total_compra = 0
contador20000 = 0
contador10000 = 0
contador5000 = 0
contador2000 = 0
contador1000 = 0
contador500 = 0
contador100 = 0
contador50 = 0
contador10 = 0
while 1:
    producto = input("ingrese producto que desea comprar: ")
    if producto == "#":
        break
    total_compra += int(producto.split(",")[1])*int(producto.split(",")[2])


print(f"El total de la compra es: {total_compra}")
pago = input("Ingrese medio de pago: ").split(",")
if pago[0] == "efectivo":
    chauchas = int(pago[1])

    vuelto = chauchas - total_compra
    while vuelto >= 10:
        if vuelto >= 20000:
            contador20000 += 1
            vuelto -= 20000
        elif vuelto >= 10000:
            contador10000 += 1
            vuelto -= 10000
        elif vuelto >= 5000:
            contador5000 += 1
            vuelto -= 5000
        elif vuelto >= 2000:
            contador2000 += 1
            vuelto -= 2000
        elif vuelto >= 1000:
            contador1000 += 1
            vuelto -= 1000
        elif vuelto >= 500:
            contador500 += 1
            vuelto -= 500
        elif vuelto >= 100:
            contador100 += 1
            vuelto -= 100
        elif vuelto >= 50:
            contador50 += 1
            vuelto -= 50
        elif vuelto >= 10:
            contador10 += 1
            vuelto -= 10
    print(f"20000: {contador20000} 10000: {contador10000} 5000: {contador5000} 2000: {contador2000} 1000: {contador1000} 500: {contador500} 100: {contador100} 50: {contador50} 10: {contador10}")

#   Otra opción P1
# Leche, 2, 1000.
# Pan, 3, 1200.
# Queso, 1, 1350.
#  Agua, 2, 380.

costo = 0
while True:
    opcion = input(
        "Ingrese el producto que desea comprar, la cantidad y valor unitario:")
    if opcion == "#":
        break
    costo = costo+(int(opcion.split(",")[1])*int(opcion.split(",")[2]))
print(f"El total de la compra es {costo}")

# 20000 10000 5000 1000
# 500 100 10
bill_20000 = 0
bill_10000 = 0
bill_5000 = 0
bill_1000 = 0
mon_500 = 0
mon_100 = 0
mon_10 = 0
mon_50 = 0
pago = input("Ingrese medio de pago y monto entregado: ")
if pago.split(",")[0] == "efectivo":
    vuelto = int(pago.split(",")[1]) - costo
    print(f"Su vuelto es {vuelto}")
    while vuelto >= 10:
        if vuelto >= 20000:
            bill_20000 = bill_20000 + 1
            vuelto = vuelto - 20000
        elif vuelto >= 10000:
            bill_10000 = bill_10000 + 1
            vuelto = vuelto - 10000
        elif vuelto >= 5000:
            bill_5000 = bill_5000 + 1
            vuelto = vuelto - 5000
        elif vuelto >= 1000:
            bill_1000 = bill_1000 + 1
            vuelto = vuelto - 1000
        elif vuelto >= 500:
            mon_500 = mon_500 + 1
            vuelto = vuelto - 500
        elif vuelto >= 100:
            mon_100 = mon_100 + 1
            vuelto = vuelto - 100
        elif vuelto >= 50:
            mon_50 = mon_50 + 1
            vuelto = vuelto - 50
        else:
            mon_10 = mon_10 + 1
            vuelto = vuelto - 10

print("Entregar ")
if bill_20000 > 0:
    print(f"{bill_20000} billetes de $20.000 ")
if bill_10000 > 0:
    print(f"{bill_10000} billetes de $10.000 ")
if bill_20000 > 0:
    print(f"{bill_5000} billetes de $5.000 ")
if bill_1000 > 0:
    print(f"{bill_1000} billetes de $1000 ")
if mon_500 > 0:
    print(f"{mon_500} monedas de $500 ")
if mon_100 > 0:
    print(f"{mon_100} monedas de $100 ")
if mon_50 > 0:
    print(f"{mon_50} monedas de $50 ")
if mon_10 > 0:
    print(f"{mon_10} monedas de $10 ")
