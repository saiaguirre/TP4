import numpy
"""La función devuelve una matriz de identidad utilizando un módulo de las
librerias de python. El usuario ingresa la longitud de la matriz y se imprime
en pantalla"""


def matriz(tamaño_matriz):
    try:
        if isinstance(tamaño_matriz, int):
            # Transforma la variable "tamaño_matriz" en integer
            # Crea la matriz identidad
            crea_iden = numpy.identity(tamaño_matriz, dtype=int)
            print(crea_iden)
            return crea_iden.tolist()
        else:
            raise ValueError
    except ValueError:
        print("No, no, Fede. Solo números enteros y positivos.")
        raise ValueError

if __name__ == "__main__":
    while True:
        try:
            tamaño_matriz = int(input("Ingrese un numero: "))
            matriz(tamaño_matriz)
            break
        except ValueError:
            print("nope")
        
        
