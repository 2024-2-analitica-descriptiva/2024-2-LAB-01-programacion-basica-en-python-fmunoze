"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""




def pregunta_06():

    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    with open("files/input/data.csv", "r", encoding="utf-8") as a:
        lineas = a.readlines()


    claves_values = {}


    for linea in lineas:
        b = linea.strip().split("	")
        diccionario_str = b[4]



        elementos = diccionario_str.split(",")
        for elemento in elementos:
            clave, valor = elemento.split(":")
            valor = int(valor)

            if clave not in claves_values:
                claves_values[clave] = []
            claves_values[clave].append(valor)


    resultado = []
    for clave, valores in claves_values.items():
        minimo = min(valores)
        maximo = max(valores)
        resultado.append((clave, minimo, maximo))


    resultado = sorted(resultado)

    return resultado

if __name__ == "__main__":
    print(pregunta_06())
