'''
​​Una inmobiliaria de una ciudad maneja una lista de inmuebles como la siguiente:
[{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'}, 
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'}, 
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'}, 
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'}, 
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

Construir una función que permita hacer búsqueda de inmuebles en función de un presupuesto dado. 
La función recibirá como entrada la lista de inmuebles y un precio, 
y devolverá otra lista con los inmuebles cuyo precio sea menor o igual que el dado. 
Los inmuebles de la lista que se devuelva deben incorporar un nuevo par a cada diccionario con el precio del inmueble, 
donde el precio de un inmueble se calcula con las siguiente fórmula en función de la zona:

Zona A: precio = (metros x 1000 + habitaciones x 5000 + garaje x 15000) x (1 - antiguedad / 100)
Zona B: precio = (metros x 1000 + habitaciones x 5000 + garaje x 15000) x (1 - antiguedad / 100) x 1.5
'''

pisos = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'}, {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'}, {'año': 1980, 'metros': 120,
                                                                                                                                                                     'habitaciones': 4, 'garaje': False, 'zona': 'A'}, {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'}, {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]


def añadir_precio(piso):
    precio = (piso['metros'] * 1000 + piso['habitaciones'] * 5000 +
              int(piso['garaje']) * 15000) * (1 - (2020 - piso['año']) / 100)
    if piso['zona'] == 'B':
        precio *= 1.5
    piso['precio'] = precio
    return piso


def busca_piso(pisos, presupuesto):
    def filtro(piso):
        return piso['precio'] <= presupuesto

    return list(filter(filtro, map(añadir_precio, pisos)))


print(busca_piso(pisos, 100000))
