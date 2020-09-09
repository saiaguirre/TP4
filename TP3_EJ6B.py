"""Función que devuelve la raiz de una función cuadrática"""


def func_raices(coef_principal, coef_secundario, term_independiente):
    coef_principal = int(coef_principal)
    coef_secundario = int(coef_secundario)
    term_independiente = int(term_independiente)
    if(coef_principal == 0):  # Si no hay coeficiente principal
        #  le pide al usuario que ingrese uno
        print("Por favor, ingrese un coeficiente principal \
diferente de 0")
    else:
        # Calcula la raiz
        raiz = (
            (coef_secundario ** 2 - 4 * coef_principal *
                term_independiente) ** 0.5)
        if isinstance(raiz, float): 
            raiz = round(raiz, 3)
            raiz_x1 = (((coef_secundario * -1) + raiz) / (coef_principal * 2))
            #raiz_y1 = ((coef_principal * (raiz_x1 ** 2)) +
            #           coef_secundario * raiz_x1 + term_independiente)
            raiz_x2 = (((coef_secundario * -1) - raiz) /
            (coef_principal * 2))
            # raiz_y2 = ((coef_principal * (raiz_x2 ** 2)) +
                    # coef_secundario * raiz_x2 + term_independiente)
            # Imprime las raices solicitadas
            print("Las raices son:", raiz_x1, "y", raiz_x2)
            return(raiz_x1, raiz_x2)
        elif isinstance(raiz, complex):
            print("Las raices son complejas y, por lo tanto no pueden ser", 
                  "calculadas en un plano bidimensional.")
            return ValueError



if(__name__ == "__main__"):
    while True:
        # Ingreso los coeficientes y el término independiente
        coef_principal = input("Por favor, ingrese el primer coeficiente: ")
        coef_secundario = input("Por favor, ingrese el segundo coeficiente: ")
        term_independiente = input(
                              "Por favor, ingrese el término independiente: ")
        try:
            func_raices(coef_principal, coef_secundario, term_independiente)
            break
        except ValueError:  
            # Avisa al usuario que hay un error y pide que
            # reingrese los valores
            print("Error al ingresar datos numéricos")