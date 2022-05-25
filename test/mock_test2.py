#   Pregunta 1

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

#   Pregunta 2
