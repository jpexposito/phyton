import unittest
import ficheromodule


"""
Test Unitarios para verificar el correcto funcionamiento del modulo
"""
class TestMyModule(unittest.TestCase):
    
    def test_lectura(self):
        self.assertEqual(ficheromodule.lectura("ficherotexto.txt"), "hola soy un fichero", "El fichero no contiene la informacion esperada")

if __name__ == "__main__":
    unittest.main()