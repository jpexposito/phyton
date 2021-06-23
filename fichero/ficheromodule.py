
"""
Funcion encargada de realizar la lectura de un fichero y mostrar el codigo por pantalla
"""
def lectura(nombre):
   result = ''
   f = open(nombre, 'r')
   try:
      for linea in f:
        result += linea + ' '
   finally:
      f.close()

   result = result[:-1]
   return result


"""
Funcion encargada de realizar la escritura de un fichero
"""
def escritura(nombre, texto):
   result = ''
   f = open(nombre, 'w')
   try:
       f.write(texto)
   finally:
      f.close()

   result = result[:-1]
   return result

