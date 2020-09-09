"""Función en la que se ingresa un número y se devuelve su equivalente en
romanos la función funciona hasta el número un millón"""


def numerosromanos(n):
        # Creo las listas de números romanos
        Unidad = ("",
                  "I",
                  "II",
                  "III",
                  "IV",
                  "V",
                  "VI",
                  "VII",
                  "VIII",
                  "IX")
        Decena = ("",
                  "X",
                  "XX",
                  "XXX",
                  "XL",
                  "L",
                  "LX",
                  "LXX",
                  "LXXX",
                  "XC")
        Centena = ("",
                   "C",
                   "CC",
                   "CCC",
                   "CD",
                   "D",
                   "DC",
                   "DCC",
                   "DCCC",
                   "CM")
        Unidad_de_mil = ("",
                         "M",
                         "MM",
                         "MMM",
                         u"I\u0305V\u0305",
                         u"V\u0305",
                         u"V\u0305I\u0305",
                         u"V\u0305I\u0305I\u0305",
                         u"V\u0305I\u0305I\u0305I\u0305",
                         u"I\u0305X\u0305")
        Decena_de_mil = ("",
                         u"X\u0305",
                         u"X\u0305X\u0305",
                         u"X\u0305X\u0305X\u0305",
                         u"X\u0305L\u0305",
                         u"L\u0305",
                         u"L\u0305X\u0305",
                         u"L\u0305X\u0305X\u0305",
                         u"L\u0305X\u0305X\u0305X\u0305",
                         u"X\u0305C\u0305")
        Centena_de_mil = ("",
                          "C\u0305",
                          "C\u0305C\u0305",
                          "C\u0305C\u0305C\u0305",
                          "C\u0305D\u0305",
                          "D\u0305",
                          "D\u0305C\u0305",
                          "D\u0305C\u0305C\u0305",
                          "D\u0305C\u0305C\u0305C\u0305",
                          "C\u0305M\u0305")
        Unidad_de_millon = ("", u"M\u0305")
        if isinstance(n, int):
                # Calcula el número ingresado en romanos
                if(n <= 1000000 and n > 0):
                        u = int(n % 10)
                        d = int((n % 100)/10)
                        c = int(n/100) % 10
                        um = int(n/1000) % 100 % 10
                        dm = int(n/10000) % 100 % 10
                        cm = int(n/100000) % 100 % 10
                        UM = int(n/1000000) % 100
                        print(str(Unidad_de_millon[UM] +
                                        Centena_de_mil[cm] +
                                        Decena_de_mil[dm] +
                                        Unidad_de_mil[um] +
                                        Centena[c] +
                                        Decena[d] + Unidad[u]))
                        num_roma = str(Unidad_de_millon[UM] +
                                       Centena_de_mil[cm] +
                                       Decena_de_mil[dm] +
                                       Unidad_de_mil[um] +
                                       Centena[c] +
                                       Decena[d] + Unidad[u])
        else:
                raise ValueError
        return num_roma
if __name__ == "__main__":
        while True:
                # Le pido que ingrese el número para transformarlo
                try:
                        n = int(input("Ingrese un número para trasformalo a" +
                                      "romanos:\n"))
                        numerosromanos(n)
                except ValueError:
                        # En caso de haber un error le aviso al usuario
                        print("Valores ingresados inválidos.")
