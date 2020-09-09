import TP3_EJ9
import unittest


class Test_EJ9(unittest.TestCase):
    def test_parametros_validos(self):
        self.assertEquals(TP3_EJ9.examen_porcentaje(10, 60, 6), "aprobó")
        self.assertEquals(TP3_EJ9.examen_porcentaje(10, 60, 5), "desaprobó")
        with self.assertRaises(ValueError):
            TP3_EJ9.examen_porcentaje(10, 60, 80)
            TP3_EJ9.examen_porcentaje(10, 110, 80)
    def test_parametros_invalidos(self):
        with self.assertRaises(ValueError):
            TP3_EJ9.examen_porcentaje(-10, "h", "|")
            TP3_EJ9.examen_porcentaje(2.3, 8.6, 10.4)
        

if __name__ == "__main__":
    unittest.main()