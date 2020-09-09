"""Función que devuelve las fichas de un dominó en orden"""


def domino():
    # La función recibe dos "For", el primero que hace que i vaya de 0 a 6
    # y el segundo hace que z vaya de un valor x a 6
    # , haciendo que luego de cada pasada se sume uno a éste valor, evitando
    # que se repitan las fichas
    x = 0
    lista=[]
    for i in range(7):
        for z in range(x, 7):
            print("---------")
            print("|", i, "-", z, "|")
            lista.append([i,z])
            print("---------")
        x += 1
    return lista
if (__name__ == "__main__"):
    domino()
