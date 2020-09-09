"""La función imprime la cantidad de números triangulares que decida solicitar
el usuario"""


def numTrian(num):
    # Declaro variables
    b = 0
    numT = 0
    # Verifico si el número está dentro de los parametros válidos
    if isinstance(num, int):
        if (num <= 0):
            raise ValueError
        # Muestro en pantalla los números triangulares
        for i in range(num):
            b += 1
            numT += b
            print(b, "-", numT)
    else:
        raise ValueError
        
    return b, "-", numT
    
    # Si no cumple los parametros de ingreso imprime un error


if __name__ == "__main__":
    while True:
        num = 0
        num = input("Ingrese el número que desee: ")
        try:
            numTrian(num)
            break
        except ValueError:
            print("Valor inválido.")