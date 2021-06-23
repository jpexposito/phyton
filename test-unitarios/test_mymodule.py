#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import mymodule


"""
Ejemplos de Test utilizando la libreria unittest
"""
class TestMyModule(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(mymodule.sum(5, 7), 12, "No se ha obtenido el resultado esperado")

    def test_error_sum(self):
        self.assertNotEqual(mymodule.sum(5, 6), 12, "El resultado obtenido debe de ser diferente 11 <> 12")


if __name__ == "__main__":
    unittest.main()