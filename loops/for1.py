'''Realice un programa que le solicite al usuario el largo del triángulo invertido y después lo despliegue por pantalla'''

# Asking the user to input a number and assigning it to the variable rows.
rows = int(input('Ingrese largo del triángulo invertido: '))
# A loop that prints the number of stars in each line.

for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("")

#   Bonus: invertir el triángulo de tal forma que quede como lo conocemos comunmente.