import TP3_EJ3
import unittest


class TestEJ3(unittest.TestCase):
    def test_numero_menor(self):
        with self.assertRaises(ValueError):
            TP3_EJ3.numTrian(-1)

    def test_palabra(self):
        with self.assertRaises(ValueError):
            TP3_EJ3.numTrian("hola")

    def test_float(self):
        with self.assertRaises(ValueError):
            TP3_EJ3.numTrian(4.5)

    def test_triangular(self):  
        comp_lista = (3, "-", 6)
        self.assertEqual(TP3_EJ3.numTrian(3), comp_lista)

if (__name__ == "__main__"):
    unittest.main()
