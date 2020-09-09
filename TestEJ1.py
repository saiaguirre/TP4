import TP3_EJ1
import unittest


class TestEJ1(unittest.TestCase):
    def test_Unicalinea(self):
        pal = "hola"
        self.assertEqual(TP3_EJ1.milPal("hola"), (pal + " ") * 1000)
if __name__ == "__main__":
    unittest.main()
