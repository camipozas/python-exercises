#   Escribir un programa que muestre la sumatoria de todos los mĂșltiplos de 7 encontrados entre el 0 y el 100.
# Summing all the multiples of 7 from 0 to 100.

total = 0

for i in range(101):
    if i % 7 == 0:
        total = total+i
print("Sumatoria de los mĂșltiplos de 7:", total)
