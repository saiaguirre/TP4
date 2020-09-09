"""Función recibe la palabra(parámetro) que imprime 1000 veces"""


def milPal(pal):
    # Devuelve la palabra en pantalla 1000 veces
        if str.isnumeric(pal):
                raise ValueError
        print((pal + " ")*1000)
        return((pal + " ")*1000)
# Se pide la palabra
if __name__ == "__main__":
        while True:
                pal = input("Ingrese la palabra deseada: ")
                try:
                        milPal(pal)
                except ValueError:
                        print("NO, no. Ingrese una palabra")
