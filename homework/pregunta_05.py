"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""



def pregunta_05():

    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
        
    with open("files/input/data.csv", "r", encoding="utf-8") as a:
        lineas = a.readlines()


    letra_values = {}


    for linea in lineas:
        b = linea.strip().split("	")
        letra = b[0]
        valor = int(b[1])


        if letra not in letra_values:
            letra_values[letra] = []
        letra_values[letra].append(valor)


    resultado = []
    for letra, valores in letra_values.items():
        minimo = min(valores)
        maximo = max(valores)
        resultado.append((letra, maximo, minimo))


    resultado = sorted(resultado)

    return resultado



if __name__ == "__main__":
    print(pregunta_05())

