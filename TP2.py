"""La función recibe dos parametros, la base y la altura y devuelve como\
   resultado su perímero"""


def a(base, altura):
    # Verifico si cumple con los requisitos de ingreso
    assert not(str.isspace(str(base))), "Ingrese un valor numérico"
    assert not(str.isspace(str(altura))), "Ingrese un valor numéricos"
    assert str.isnumeric(str(base)), "Ingrese valores numéricos"
    assert str.isnumeric(str(altura)), "Ingrese valores numéricos"
    assert int(base) > 0, "No se puede ingresar valores negativos"
    assert int(altura) > 0, "No se puede ingresar valores negativos"
    # Imprimo en pantalla el perímetro
    print("Perimetro = ", int(base)*2+int(altura)*2)
    return(int(base)*2+int(altura)*2)
"""La función recibe dos parametros, la base y la altura y devuelve como\
   resultado su area"""


def b(base, altura):
    # Verifico si cumple con los requisitos de ingreso
    assert not(str.isspace(str(base))), "Ingrese un valor numérico"
    assert not(str.isspace(str(altura))), "Ingrese un valor numérico"
    assert str.isnumeric(str(base)), "Ingrese valores numéricos"
    assert str.isnumeric(str(altura)), "Ingrese valores numéricos"
    assert int(base) > 0, "No se puede ingresar valores negativos"
    assert int(altura) > 0, "No se puede ingresar valores negativos"
    # Imprimo en pantalla el area
    print("Area = ", int(base)*int(altura))
    return(int(base)*int(altura))
"""Función que recibe 4 parametro con 4 coordenadas y devuelve como \
   resultado el Area entre esas coordenadas"""


def c(x1, x2, x3, x4):
    # Guardo las coordenadas en una sola variable
    puntos = [x1, x2, x3, x4]
    # Verifico si cumplen con los requisitos de ingreso
    for x in puntos:
        for i in [0, 1]:
            assert not(str.isspace(str(x[i]))), "Ingresó incorrectamente \
alguna(s) de la(s) coordenada(s)"
            assert str.isnumeric(str(x[i])), "Por favor, ingrese valores \
numéricos en las coordenadas"
            assert int(x[i]) > 0, "No se pueden ingresar valores negativos en \
las coordenadas"
    # Calculo su base y altura y los guardo en variables
    altura = abs(int(x1[1])-int(x3[1]))
    base = abs(int(x3[0])-int(x4[0]))
    # En caso de que su base o altura den 0
    if altura == 0:
        altura = abs(int(x2[1])-int(x3[1]))
    elif base == 0:
        base = abs(int(x2[0])-int(x3[0]))
    # Imprimo en pantalla el area
    print("Area = ", altura*base)
    return(altura*base)
"""Función que recibe un parametro y devuelve el perímetro y el\
   area de una circunferencia"""


def d(radio):
    # Verifico si cumplen con los requisitos de ingreso
    assert not(str.isspace(str(radio))), "Ingrese un valor numérico para el \
radio"
    assert str.isnumeric(str(radio)), "Ingrese un valor numérico para el \
radio"
    assert float(radio) > 0, "Ingrese valores positivos para el radio"
    # Imprimo en pantalla el perímetro
    print("Perimetro = ", 3.14*float(radio)*2)
    # Imprimo en pantalla el area
    print("Area = ", 3.14*(float(radio)**2))
    # Guardo el perímetro y el area en variables
    Perimetro = 3.14*float(radio)*2
    Area = 3.14*(float(radio)**2)
    return(Perimetro, Area)
"""Función que recibe un parámetro y devuelve como resultado\
   el volumen de una esfera"""


def e(radio):
    # Verifico si cumplen con los requisitos de ingreso
    assert not(str.isspace(str(radio))), "Ingrese un valor numérico para el \
radio"
    assert str.isnumeric(str(radio)), "Ingrese un valor numerico para el\
radio"
    assert float(radio) > 0, "Ingrese valores positivos para el radio"
    # Imprimo en pantalla el area
    print('Volumen = ', 1.333333*3.14*(float(radio)**3))
    return(1.333333*3.14*(float(radio)**3))


if (__name__ == "__main__"):
    # Se ingresan los datos para los parámetros de las funciones
    x1 = [0, 1]
    x2 = [0, 1]
    x3 = [0, 1]
    x4 = [0, 1]
    while True:
        base = input('base: ')
        altura = input('altura: ')
        try:
            a(base, altura)
            b(base, altura)
            break
        except AssertionError as Error:
            print(Error)
            continue
    while True:
        x1[0] = (input("x1: "))
        x1[1] = (input("y1: "))
        x2[0] = (input("x2: "))
        x2[1] = (input("y2: "))
        x3[0] = (input("x3: "))
        x3[1] = (input("y3: "))
        x4[0] = (input("x4: "))
        x4[1] = (input("y4: "))
        try:
            c(x1, x2, x3, x4)
            break
        except AssertionError as Error_coor:
            print(Error_coor)
            continue
    while True:
        radio = input('Radio: ')
        try:
            d(radio)
            break
        except AssertionError as Error:
            print(Error)
            continue
    while True:
        radio = (input('Radio esfera: '))
        try:
            e(radio)
            break
        except AssertionError as Error:
            print(Error)
            continue
