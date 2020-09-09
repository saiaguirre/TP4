import TP3_EJ6A
import TP3_EJ6B
import TP3_EJ6C
import unittest


class Test_EJ6(unittest.TestCase):
    def test_res_correctos(self):
        self.assertEquals(TP3_EJ6A.func_max_min(2, 3, 7,), (-0.75, 5.875))
        self.assertEquals(TP3_EJ6B.func_raices(2, 3, 7), ValueError)
        self.assertEquals(TP3_EJ6C.intersec_rectas(2, 3, 7, 8), (1, 5))

    def test_valores_no_num(self):
        with self.assertRaises(ValueError):
            TP3_EJ6A.func_max_min("a", "*", "-1")
            TP3_EJ6B.func_raices("a", 5 ** 0.5, "<")
            TP3_EJ6C.intersec_rectas("a", "#", "6", "|")
if __name__ == "__main__":
    unittest.main()
