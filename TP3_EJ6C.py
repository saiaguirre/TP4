"""Función que calcula la intersección entre dos rectas ingresadas
 por el usuario"""


def intersec_rectas(pendiente1, ordenada1, pendiente2, ordenada2):
    pendiente1 = int(pendiente1)
    ordenada1 = int(ordenada1)
    pendiente2 = int(pendiente2)
    ordenada2 = int(ordenada2)

    if pendiente1 == pendiente2 and ordenada1 == ordenada2:
        # Le avisa al usuario si ingreso dos rectas iguales
        print("La rectas son iguales se cruzan en infinitos puntos")
        intersec_rectas(pendiente1, ordenada1, pendiente2, ordenada2)
    elif pendiente1 == pendiente2:  # Le avisa al usuario si
        # son paralelas
        print("Son paralelas no tiene intersecciones")
        intersec_rectas(pendiente1, ordenada1, pendiente2, ordenada2)
    else:
        # Calcula la intersección de las rectas
        punto_x = (ordenada1 - ordenada2) / (pendiente1 - pendiente2)
        punto_y = pendiente1 * punto_x + ordenada1
        # Imprime los puntos
        print("La intersección es en el punto x:", punto_x,
                "e y:", punto_y)
    return(punto_x, punto_y)

if(__name__ == "__main__"):
    while True:
        # Ingreso la pendiente y la ordenada de origen de las rectas
        pendiente1 = input("Ingrese la pendiente de la recta: ")
        ordenada1 = input("Ingrese la ordenada de la recta: ")
        pendiente2 = input("Ingrese la pendiente de la segunda recta: ")
        ordenada2 = input("Ingrese la ordenada de la segunda recta: ")
        try:  
            # Pruebo si cumple con los parámetros debidos
            intersec_rectas(pendiente1, ordenada1, pendiente2, ordenada2)
            break
        except ValueError:  # Le informa al usuario si hay un error
            print("Error al ingresar datos numéricos.")
