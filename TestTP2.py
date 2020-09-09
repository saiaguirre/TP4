import TP2
import unittest


class Test_TP2(unittest.TestCase):
    def test_perímetro1(self):
        with self.assertRaises(AssertionError):
            TP2.a("hola", "pedro")

    def test_perímetro2(self):
        with self.assertRaises(AssertionError):
            TP2.a(2, None)

    def test_perímetro3(self):
        with self.assertRaises(AssertionError):
            TP2.a(-2, -1)

    def test_perímetro4(self):
        self.assertEqual(TP2.a(2, 2), 8)

    def test_area1(self):
        with self.assertRaises(AssertionError):
            TP2.b("x", "jesus")

    def test_area2(self):
        with self.assertRaises(AssertionError):
            TP2.b(2, -1)

    def test_area3(self):
        with self.assertRaises(AssertionError):
            TP2.b(None, None)

    def test_area4(self):
        self.assertEqual(TP2.b(2, 2), 4)

    def test_coor1(self):
        x1 = ["hola", 3]
        x2 = ["s", 2]
        x3 = [2, 3]
        x4 = [2, "we"]
        with self.assertRaises(AssertionError):
            TP2.c(x1, x2, x3, x4)

    def test_coor2(self):
        x1 = [None, 3]
        x2 = [None, 2]
        x3 = [2, 3]
        x4 = [2, None]
        with self.assertRaises(AssertionError):
            TP2.c(x1, x2, x3, x4)

    def test_coor3(self):
        x1 = [-7, 3]
        x2 = [5, 2]
        x3 = [-2, 3]
        x4 = [2, -2]
        with self.assertRaises(AssertionError):
            TP2.c(x1, x2, x3, x4)

    def test_coor4(self):
        x1 = [2, 4]
        x2 = [3, 6]
        x3 = [3, 6]
        x4 = [2, 4]
        self.assertEqual(TP2.c(x1, x2, x3, x4), 2)

    def test_radio1(self):
        with self.assertRaises(AssertionError):
            TP2.d("hola")

    def test_radio2(self):
        with self.assertRaises(AssertionError):
            TP2.d(None)

    def test_radio3(self):
        with self.assertRaises(AssertionError):
            TP2.d(-2)

    def test_radio4(self):
        self.assertEqual(TP2.d(2), (12.56, 12.56))

    def test_radio_esfera1(self):
        with self.assertRaises(AssertionError):
            TP2.e("gege")

    def test_radio_esfera2(self):
        with self.assertRaises(AssertionError):
            TP2.e(None)

    def test_radio_esfera3(self):
        with self.assertRaises(AssertionError):
            TP2.e(-2)

    def test_radio_esfera3(self):
        self.assertEqual(TP2.e(1), 4.18666562)

if(__name__ == "__main__"):
    unittest.main()
