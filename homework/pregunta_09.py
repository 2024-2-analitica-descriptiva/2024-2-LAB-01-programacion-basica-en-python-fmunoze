"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""




def pregunta_09():

    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

    with open("files/input/data.csv", "r", encoding="utf-8") as a:
        lineas = a.readlines()


    conteo_claves = {}


    for linea in lineas:
        columnas = linea.strip().split("	")
        columna_5 = columnas[4]


        pares = columna_5.split(",")
        for par in pares:
            clave, _ = par.split(":")
            if clave not in conteo_claves:
                conteo_claves[clave] = 0
            conteo_claves[clave] += 1

    return conteo_claves

if __name__ == "__main__":
    print(pregunta_09())