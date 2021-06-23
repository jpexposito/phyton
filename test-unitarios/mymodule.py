#!/usr/bin/env python

""" Programa destinado a apoyar la explicacion de test unitarios dentro de Phyton """

""" La función sum obtiene dos numeros (enteros o de coma flotante) y retorna el
resultado de su suma. Si se ingresan valores que no sean del tipo comentado
anteriormente, se lanza la excepcion TypeError """
def sum(a, b):
   """
    Retorna a + b.
    
    >>> sum(5, 7)
    12
    >>> sum(5, "Python")
    Traceback (most recent call last):
        ...
    TypeError
    """
   for n in (a, b):
        if not isinstance(n, int) and not isinstance(n, float):
            raise TypeError
   return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)   
