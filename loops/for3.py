#   Escribir un programa que muestre la sumatoria de todos los múltiplos de 7 encontrados entre el 0 y el 100.

total = 0

for i in range(101):
    if i % 7 == 0:
        total = total+i
print("Sumatoria de los múltiplos de 7:", total)
