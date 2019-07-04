from comparar import comparar
import unittest
import os
class  TestStringMethods(unittest.TestCase ):
    def test_complejidad_decision(self):
        var = os.system('xenon -b A decision.py')
        valor= 0

        self.assertEqual(var, valor)

    def test_complejidad_Read(self):
        var = os.system('xenon -b B Read.py')
        valor = 0

        self.assertEqual(var, valor)

if __name__ == '__main__':
    unittest.main()