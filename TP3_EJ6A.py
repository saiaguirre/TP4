"""Función para obtener el máximo o mínimo de una función cuadrática
ingresada"""


def func_max_min(coef_principal, coef_secundario, term_independiente):
    coef_principal = int(coef_principal) 
    coef_secundario = int(coef_secundario) 
    term_independiente = int(term_independiente)
    if(coef_principal == 0):  
        # Si no hay coeficiente principal le pide al usuario que ingrese uno
        print("Error, el primer coeficiente no puede ser igual a 0")
        func_princ()
    else:
        # Fórmula para sacar el X del mínimo o máximo
        vertice_x = (coef_secundario * -1) / (coef_principal * 2)
        vertice_y = ((coef_principal * (vertice_x ** 2)) +
                        coef_secundario * vertice_x + term_independiente)
        if coef_principal < 0:  # Verifica si es un máximo
            # Imprime las coordenadas del máximo
            print("El máximo se encuentra en",
                    vertice_x, "de X y", vertice_y, "de Y")
        elif coef_principal > 0:  # Verifica si es un mínimo
            # Imprime las coordenadas del mínimo
            print("El mínimo se encuentra en",
                    vertice_x, "de X y", vertice_y, "de Y")
    return(vertice_x, vertice_y)


def func_princ():
    if __name__ == "__main__":
        while True:
            # Ingreso los coeficientes y el término independiente
            coef_principal = input("Por favor, ingrese el primer coeficiente: ")
            coef_secundario = input("Por favor, ingrese el segundo coeficiente: ")
            term_independiente = input(
                                "Por favor, ingrese el término independiente: ")
            try:
                func_max_min(coef_principal, coef_secundario, term_independiente)
                break
            except ValueError:  
                # Avisa al usuario que hay un error y pide que
                # reingrese los valores
                print("Error al ingresar datos numéricos")
func_princ()
