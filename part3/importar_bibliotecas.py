"""
from random import randint

valor = randint (1, 10)
print(valor)

"""

"""
Confeccionar un programa que solicite la carga de un valor entero por teclado y luego nos muestre la raíz cuadrada del número y el valor elevado al cubo.

from math import sqrt, pow

valor = int(input("Ingresa el valor: "))
raiz = sqrt (valor)
cubo = pow (valor, 3)

print("La raíz cuadrada del numero es: ", raiz)
print("El valor elevado al cubo es: ", cubo)

"""

"""
from math import sqrt as raiz, pow as elevador

valor = int(int(input("Ingresa el valor: ")))

raiiz = raiz (valor)
cubo = elevador (valor, 3)

print("La raíz cuadrada del numero es: ", raiiz)
print("El valor elevado al cubo es: ", cubo)

"""

"""
Calcular el factorial de un número ingresado por teclado.
El factorial de un número es la cantidad que resulta de la multiplicación de determinado número natural por todos los números naturales que le anteceden excluyendo el cero. Por ejemplo el factorial de 4 es 24, que resulta de multiplicar 4*3*2*1.
No hay que implementar el algoritmo para calcular el factorial sino hay que importar dicha funcionalidad del módulo math.
El módulo math tiene una función llamada factorial que recibe como parámetro un entero del que necesitamos que nos retorne el factorial.
Solo importar la funcionalidad factorial del módulo math de la biblioteca estándar de Python.

from math import factorial as factor

y = int(input("Ingrese el numero para calcular el factorial: "))
fact = factor (y)
print("El factorial del numero es: ", fact)

"""



