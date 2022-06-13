import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

archivo = pd.read_excel('Sales-ACME.xls')

'''
1. Limpie los datos (filas o columnas vacías).
'''
# Elimina una columna si faltan *todos* los datos
archivo.dropna(axis=1, how="all", inplace=True)
# Elimina una fila si falta *algún* dato
archivo.dropna(axis=0, how="any", inplace=True)

'''
2. Cree una nueva variable llamada Venta la cual corresponde al producto entre las
unidades vendidas y su respectivo precio.
3. De la misma forma, agregue la variable Costo pero considerando aquel costo por unidad.
4. Agregue una columna llamada Utilidad que corresponde a la diferencia entre (2) y (3).
'''
archivo["Venta"] = archivo["Units Sold"] * archivo["Unit Price"]
archivo["Costo"] = archivo["Units Sold"] * archivo["Unit Cost"]
archivo["Utilidad"] = archivo["Venta"] - archivo["Costo"]

'''
5. ¿Cuál es la venta, costo y utilidad total?
'''
print("Venta total:", archivo["Venta"].sum())
print("Costo total:", archivo["Costo"].sum())
print("Utilidad total:", archivo["Utilidad"].sum())
print("")

'''
6. Calcule la media, desviación estándar, máximo, mínimo y/o algún otro indicador que usted
considere pertinente.
'''
utilidad = archivo["Utilidad"]
print("ESTADÍSTICAS DE LAS UTILIDADES: ")
print("  - Media:", utilidad.mean())
print("  - Desviación estándar:", utilidad.std())
print("  - Máximo:", utilidad.max())
print("  - Mínimo:", utilidad.min())
print("")

'''
7. Cree una función que reciba la región y devuelva el total de ventas por región.
Acompáñelo con un gráfico. Muéstrelo para todas las regiones.
'''


def total_ventas_region(archivo, region):
    datos_region = archivo[archivo["Region"] == region]
    total_ventas = datos_region["Venta"].sum()

    ventas_por_pais = datos_region.groupby(
        "Country", as_index=False)["Venta"].sum()
    paises = ventas_por_pais["Country"]
    ventas = ventas_por_pais["Venta"]
    plt.bar(paises, ventas)
    plt.xticks(range(len(paises)), paises, rotation=90)
    plt.show()

    return total_ventas


for region in archivo["Region"].unique():
    print(region)
    print("    - Total de ventas:", total_ventas_region(archivo, region))
    print("")

'''
8. Cree una función que reciba el archivo y devuelva las 5 regiones con mayor utilidad.
'''


def top_5_utilidad_regiones(archivo):
    utilidades_por_region = archivo.groupby(
        "Region", as_index=False)["Utilidad"].sum()
    top_5 = utilidades_por_region.nlargest(5, "Utilidad")

    print(top_5)


top_5_utilidad_regiones(archivo)

'''
9. Exporte el archivo como Excel incluyendo las columnas agregadas. El nombre del archivo
debe ser la fecha de hoy.
'''
archivo.to_excel('13-06-2022.xls')
