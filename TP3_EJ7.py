"""Función que devuelve el día del número del año que haya ingresado
teniendo en cuenta si el año empezara un lunes"""


def quedia(n):
    # Creo la lista de los días
    dias = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes",
            "Sábado"]
    # Calcula el número del año ingresado y le asigna un día
    n = int(n)
    if n >= 1 and n <= 366:
        n = n % 7
        print("el día es", dias[n])
        return dias[n]  
    else:
        print("Número inválido")
        pass
        


if __name__ == "__main__":
# Pido que ingrese el día
    while True:
        n = (input("Ingrese un número de día entre 1 y 366: ")) 
        try:
            quedia(n)
        except ValueError:  # Le avisa al usuario si hay un error
            print("Número inválido")
