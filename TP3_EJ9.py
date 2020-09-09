"""Función en la que ingreso la cantidad de ejercicios de un examen y el
porcentaje necesario para aprobar y según cuantos ejercicios haya hecho el
alumno devuelve en pantalla si aprobó o no"""


def examen_porcentaje(cant_ej, porcent_ej, ej_correctos):
    if not isinstance(cant_ej, int) or (cant_ej <= 0):
        raise ValueError
    if not isinstance(porcent_ej, int) or (porcent_ej <= 0):
        raise ValueError
    if not isinstance(ej_correctos, int) or (ej_correctos <= 0):
        raise ValueError
    try:
        if(not isinstance(ej_correctos, int) or (ej_correctos <= 0) or
            (ej_correctos > cant_ej)):
            raise ValueError
    except ValueError:
        print("Ingrese un valor númerico dentro del rango de 0",
                "a " + str(cant_ej))
        raise ValueError
    # ValueErrors
    if(ej_correctos < 0):
        raise ValueError
    elif(ej_correctos > cant_ej):
        raise ValueError
    else:
        porcent_alumno = (ej_correctos * 100) / cant_ej
    # Verifica si el alumno aprobó o no
    if(porcent_alumno >= porcent_ej):
        print("El alumno aprobó con el " +
                str(porcent_alumno) + "%")
        return "aprobó"
        examen_porcentaje()
    else:
        print("El alumno desaprobó con el " +
                str(porcent_alumno) + "%")
        return "desaprobó"
        examen_porcentaje()
    # Devuelve un error en caso de datos mal ingresados


def func_prim():
        while True:
            try:
                # Ingreso la cantidad de ejercicios
                print("Recuerde ingresar un asterisco en la cantidad de",
                      "ejercicios realizados por el alumno para terminar el",
                      "programa")
                cant_ej = int(input("Ingrese la cantidad de ejercicios del exámen: "))
                # Ingreso el porcentaje que debe estar correcto
                porcent_ej = int(input("Ingrese el porcentaje de ejercicios que " +
                                    "deben estar aprobados: "))
                ej_correctos = input("¿Cuántos ejercicios correctos " +
                                         "hizo el alumno? ")
                if not ej_correctos == "*":
                    try:
                        ej_correctos = int(ej_correctos)
                    except ValueError:
                        print("Valor ingresado inválido.")
                else:
                    quit()
                examen_porcentaje(cant_ej, porcent_ej, ej_correctos)
            except ValueError:
                print("Valores no numéricos inválidos ingresados.")
if __name__ == "__main__":
    func_prim()