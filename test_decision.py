from comparar import comparar
import unittest
import os
class  TestStringMethods(unittest.TestCase ):
    def test_complejidad(self):
        var = os.system('xenon -b B decision.py')
        valor= 0
        self.assertEqual(var, valor)


if __name__ == '__main__':
    unittest.main()