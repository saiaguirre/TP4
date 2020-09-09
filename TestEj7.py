import TP3_EJ7
import unittest


class Test_EJ7(unittest.TestCase):
    def test_dia(self):
        self.assertEquals(TP3_EJ7.quedia(1), "Lunes")
        self.assertEquals(TP3_EJ7.quedia(2), "Martes")
        self.assertEquals(TP3_EJ7.quedia(3), "Miércoles")
        self.assertEquals(TP3_EJ7.quedia(4), "Jueves")
        self.assertEquals(TP3_EJ7.quedia(5), "Viernes")
        self.assertEquals(TP3_EJ7.quedia(6), "Sábado")
        self.assertEquals(TP3_EJ7.quedia(7), "Domingo")
        self.assertEquals(TP3_EJ7.quedia(274), "Lunes")
    def num_nega(self):
        self.assertEquals(TP3_EJ7.quedia(-1), ValueError)
    def no_num(self):
        self.assertEquals(TP3_EJ7.quedia("-"), ValueError)
        self.assertEquals(TP3_EJ7.quedia("a"), ValueError)
        self.assertEquals(TP3_EJ7.quedia(), ValueError)


if __name__ == "__main__":
    unittest.main()