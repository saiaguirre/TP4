import TP3_EJ8
import unittest


class Test_EJ8(unittest.TestCase):
    def test_num_roma(self):
        self.assertEquals(TP3_EJ8.numerosromanos(5), "V")
        self.assertEquals(TP3_EJ8.numerosromanos(15), "XV")
        self.assertEquals(TP3_EJ8.numerosromanos(999999), "C̅M̅X̅C̅I̅X̅CMXCIX")
    def test_no_valid_char(self):
        with self.assertRaises(ValueError):
            TP3_EJ8.numerosromanos("a")
            TP3_EJ8.numerosromanos("*")
            TP3_EJ8.numerosromanos(-4)
            TP3_EJ8.numerosromanos(0)
            tp3.ej8.numerosromanos(8.3)

if __name__ == "__main__":
    unittest.main()