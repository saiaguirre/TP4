import TP3_EJ5
import unittest
import numpy as np


 class Test_EJ5(unittest.TestCase):
     def test_matriz(self):
        matriz = np.identity(5, dtype=int)
        self.assertEquals(TP3_EJ5.matriz(5), matriz.tolist())

    def test_val(self):
        with self.assertRaises(ValueError):
            TP3_EJ5.matriz(2.3)
            TP3_EJ5.matriz(-1)
            TP3_EJ5.matriz("|")

if __name__ == "__main__":
    unittest.main()