#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Lista(): #Creamos la clase Lista
   def __init__(self, list_in =None): #Definimos el parametro list_int
      self.list_in = list_in # Asignamos valor al atributo file_int
        
   """
      Funcion encargada de realizar verificar si una lista es creciente
   """
   def es_creciente(self, lista):
      actual = anterior= 0
      creciente = True
      tam = len(lista)
      while (creciente == True) and ((actual +1) < tam):
         for i in range(1, len(lista)):
               anterior = actual
               actual = i
               if lista[anterior] >= lista[actual]:
                  creciente = False
                  
      return creciente

   """
      Funcion encargada de invertir una lista
   """
   def inversa(self, lista):
      return list(reversed(lista))
