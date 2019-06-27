from comparar import comparar
import unittest

class  TestStringMethods(unittest.TestCase ):
    def test_exito(self):

        var = comparar(4,2,3)
        valor= 1
        self.assertEqual(var, valor)

    def test_iguales(self):
        var= comparar(1,2,2)
        valor=0
        self.assertEqual(var, valor)


if __name__ == '__main__':
    unittest.main()