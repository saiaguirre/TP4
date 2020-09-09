import TP3_EJ4
import unittest


class Test_Ej4(unittest.TestCase):
    def test_coor(self):
        lista = ([10.296, 5, 9], 1, None)
        self.assertEquals(TP3_EJ4.func_logica((2, 4, 5), (3, 7, 9)), lista)

    def test_char(self):
        with self.assertRaises(ValueError):
            TP3_EJ4.func_logica(["a", "e", 4], [4, 1, "q"])

    def test_nada(self):
        with self.assertRaises(ValueError):
            TP3_EJ4.func_logica([], [])

    def test_dos_punt_iguales(self):
        lista_text = ([7.071, 5, 5], 2, "Hay más de un punto")
        self.assertEquals(TP3_EJ4.func_logica((5, 5, 3), (5, 5, 2)),
                          lista_text)

    

if (__name__ == "__main__"):
    unittest.main()