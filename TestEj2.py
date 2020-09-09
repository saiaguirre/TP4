import TP3_EJ2 
import unittest

class Test_ej2(unittest.TestCase):
    def test_domino2(self):
        lista_prueba = [[0, 0],[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 1], [1, 2], [1,3], [1,4], [1,5], [1,6], [2,2], [2,3], [2,4], [2,5], [2,6], [3,3], [3,4], [3,5], [3,6], [4,4], [4,5], [4,6], [5,5], [5,6], [6,6] ]
        self.assertEquals(TP3_EJ2.domino(),lista_prueba)
if (__name__ == "__main__"):
    unittest.main()