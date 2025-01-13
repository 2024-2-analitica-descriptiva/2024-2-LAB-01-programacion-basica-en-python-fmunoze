"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""



def pregunta_12():

    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    with open("files/input/data.csv", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()


    suma_por_columna_1 = {}

    for linea in lineas:
        columnas = linea.strip().split("	")
        letra_columna_1 = columnas[0]
        pares_columna_5 = columnas[4].split(",")


        suma_columna_5 = sum(int(par.split(":")[1]) for par in pares_columna_5)


        if letra_columna_1 in suma_por_columna_1:
            suma_por_columna_1[letra_columna_1] += suma_columna_5
        else:
            suma_por_columna_1[letra_columna_1] = suma_columna_5

    return suma_por_columna_1

if __name__ == "__main__":
    print(pregunta_12())
