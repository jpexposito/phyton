# TEST-UNITARIOS
Este ejemplo trata de introducir el concepto de test, para verificar si un módulo o conjunto de ellos funciona correctamente. El concepto Unit Test no se limita a un lenguaje específico, si no a una herramienta durante el ciclo de desarrollo de nuestro proyecto. Las pruebas unitarias se implementan de forma parelela al desarrollo, y se ejecutan para garantizar el correcto funcionamiento de nuestro proyecto. La clave para el correcto desarrollo del código y las pruebas unitarias, consiste en separar las responsabilidades, de modo que los test sólo deben comprobar que el código funciona correctamente.

## ¿Cuando utilizar las pruebas unitarias?
   __Siempre__. Cuando desarrolles un módulo o un paquete que provee una API (conjunto de funciones y clases) debes de crear las pruebas unitarias que garanticen el correcto funcionamiento de esta.

## ¿Cómo implementarlo en Python?
Existen diversos frameworks para implementar pruebas unitarias. En este ejemplo se mostrarán dos de ellos: unittest y doctest. El primero es un tanto arcaico y derivado de otros lenguajes, aunque no menos eficiente. El segundo es tal vez más pythonico. Veremos las características generales de ambos a través un ejemplo, quédate con el que te sientas más a gusto.

### Unittest
*Unittest* provee una serie de funciones de las que haremos uso para verificar a través de test, dentro de ficheros específicos (ej:test_mymodelu.py), el correcto funcionamiento de nuestros módulos. Algunas de esas funciones son las siguientes:

#### Función	Operación equivalente
##### assertEqual(a, b)	a == b
##### assertNotEqual(a, b)	a != b
##### assertTrue(x)	bool(x) is True
##### assertFalse(x)	bool(x) is False
##### assertIs(a, b)	a is b
##### assertIsNot(a, b)	a is not b
##### assertIsNone(x)	x is None
##### assertIsNotNone(x)	x is not None
##### assertIn(a, b)	a in b
##### assertNotIn(a, b)	a not in b
##### assertIsInstance(a, b)	isinstance(a, b)
##### assertNotIsInstance(a, b)	not isinstance(a, b)

En el ejemplo que se ha realizado obtendremos la siguiente salida:
```
test_mymodule.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s
OK
```
### Doctest

La implementación de la prueba unitaria utilizando doctest se realiza junto con la documentación de una función o clase. Por ejemplo, siguiendo con nuestra función original sum, añadiremos una breve descripción en la documentación.
```
   """
    Retorna a + b.
    
    >>> sum(5, 7)
    12
    >>> sum(5, "Python")
    Traceback (most recent call last):
        ...
    TypeError
    """
```
Además debes de incluir dentro del módulo la siguiente sintaxis:
```
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
```
Para ejecutarlo finalmente debes de ejecutar la siguiente sentencia:
```
python3 -m doctest -v mymodule.py
```
Obtendrás una salida como la siguiente:
```
Trying:
    sum(5, 7)
Expecting:
    12
ok
Trying:
    sum(5, "Python")
Expecting:
    Traceback (most recent call last):
        ...
    TypeError
ok
1 items had no tests:
    mymodule
1 items passed all tests:
   2 tests in mymodule.sum
2 tests in 2 items.
2 passed and 0 failed.
Test passed.
```
## Siempre recuerda
Cuando realizas test, te auto ayudas a tí y sobre ayudas a todos aquellos desarrolladores que toquen el código después de tí, ya que tendrán una herramienta con la que evaluar el desarrollo y realizar una entrega con confianza del proyecto.

## Sigue aprendiendo
Si quieres leer algo sobre test, aquí tienes un enlace https://jpexposito.com/junit-test-and-code-coverage/

## Recuerda
Desarrolla con cariño, es la base de dejar un código que comprenderá tu abuela.
