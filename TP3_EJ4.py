

def func_distancia():
    # Asigno variables y listas
    i = 0
    lista_x = []
    lista_y = []
    while(i < 3):
        # Pido que ingrese los valores de los puntos 3 veces
        val_x = input("Ingrese el valor de X: ")
        val_y = input("Ingrese el valor de Y: ")
        i += 1
        try:
            # Compruebo que lo ingresado sea un número
            val_x = int(val_x)
            val_y = int(val_y)
            # Agrego los valores a las listas para compararlos luego
            lista_x.append(val_x)
            lista_y.append(val_y)
        except ValueError:
            print("Error al ingresar valores numéricos. ")
            i = 0
    dist_fin, cant_dist, var_control = func_logica(lista_x, lista_y)
    if(cant_dist == 1):
        print("La mayor distancia registrada fue", dist_fin[0],
              "unidades. Las coordenadas de éste punto son:", dist_fin[1],
              "en X y", dist_fin[2], "en Y.")
    if(cant_dist > 1):
        print("Se encontraron", cant_dist, "puntos con igual distancia desde",
              "el centro de coordenadas, siendo ésta", dist_fin[0])


def func_logica(lista_x, lista_y):
    val_control = 0
    i = 0
    h = 0
    try:
        if len(lista_x) != 3 or len(lista_y) != 3:
            # Si las listas tienen más o menos cantidad de caracteres que los
            # dictados por el ejercicio, salta un error.
            raise ValueError
        for i in range(3):
            # En caso de que cualquiera de los elementos de ambas listas NO
            # sea un número natural entero, salta un error.
            if not isinstance(lista_x[i], int):
                raise ValueError
            if not isinstance(lista_y[i], int):
                raise ValueError
    except ValueError:
        raise ValueError
    dist = 0
    _ = 0
    cant_dist = 1
    list_dist = []
    dist_fin = []
    una_dist = 0
    for _ in range(3):
        dist = round((((lista_x[_] ** 2) + (lista_y[_] ** 2)) ** 0.5), 3)
        if(dist == una_dist):
            cant_dist += 1
            list_dist.append(dist)
        if(dist > una_dist):
            if(cant_dist == 2):
                cant_dist -= 1
            una_dist = dist
            dist_fin = [dist, lista_x[_], lista_y[_]]
            print(list_dist)
    if cant_dist > 1:
        var_control = "Hay más de un punto"
        return dist_fin, cant_dist, var_control
    else:
        return dist_fin, cant_dist, None
if(__name__ == "__main__"):
    func_distancia()