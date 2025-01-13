"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""




def pregunta_11():

    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """

    with open("files/input/data.csv", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()


    suma_por_letra = {}

    for linea in lineas:
        columnas = linea.strip().split("	")
        valor_columna_2 = int(columnas[1])
        letras_columna_4 = columnas[3].split(",")


        for letra in letras_columna_4:
            if letra in suma_por_letra:
                suma_por_letra[letra] += valor_columna_2
            else:
                suma_por_letra[letra] = valor_columna_2


    return dict(sorted(suma_por_letra.items()))

if __name__ == "__main__":
    print(pregunta_11())
