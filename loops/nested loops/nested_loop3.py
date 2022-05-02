'''
#   TODO: Ordenamiento por bubble sort
Fernando Cuevas desea jugar los siguientes 10 números en la lotería [3,8,7,25,15,33,21,12,9,14]. 
Realice un programa en python utilizando ciclos anidados que ordene de menor a mayor 
los números elegidos por Fernando Cuevas y los imprima por pantalla. 
'''

lista = [3, 8, 7, 25, 15, 33, 21, 12, 9, 14]
for i in range(0, len(lista)):
    for j in range(0, len(lista)-1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]
print(lista)
