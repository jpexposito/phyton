#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import listas as ListaClass


"""
Ejemplos de Test utilizando la libreria unittest
"""
class TestClaseLista(unittest.TestCase):
    
    lista = None
    lista_in = None

    @classmethod
    def setUpClass(cls):
        cls.lista = ListaClass.Lista() #se realiza la instancia de la clase lista
        cls.lista_in = [1, 2, 3, 4]

    """
        Test que verifica que la funcion es_creciente verifica correctamente una lista
    """
    def test_es_creciente(self):
        resultado = self.lista.es_creciente(self.lista_in)
        self.assertTrue(resultado == True, "La lista creciente no retorna el resultado esperado = true")
    """
        Test que verifica que una lista se invierte de forma correcta
    """
    def test_inversa(self):
        inversa = self.lista.inversa(self.lista_in)
        self.assertEqual(self.lista_in[3], inversa[0] , "La no se ha invertido correctamente ")

if __name__ == "__main__":
    unittest.main()