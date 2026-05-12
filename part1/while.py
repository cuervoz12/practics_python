"""
Realizar un programa que imprima en pantalla los números del 1 al 100.

Sin conocer las estructuras repetitivas podemos resolver el problema empleando una estructura secuencial. Iniciamos una variable con el valor 1, luego imprimimos la variable, 
incrementamos nuevamente la variable y así sucesivamente.

x =1
while x <= 99:
    x += 1
    print(x)

""" 

"""
Codificar un programa que solicite la carga de un valor positivo y nos muestre desde 1 hasta el valor ingresado de uno en uno.
Ejemplo: Si ingresamos 30 se debe mostrar en pantalla los números del 1 al 30.


n = int(input('Ingrese un valor '))
x  = 1
while x < n:
    x += 1
    print (x) 
"""  

"""  
Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre posteriormente la suma de los valores ingresados y su promedio.

  

x = 1
y = 0
suma = 0
promedio = 0
while  x <= 10:
    y = int(input('Ingrese 10 valores: '))
    suma += y
    promedio = suma/10
    x += 1 

print('la suma es: ', suma)
print('El promedio es: ',promedio)   
"""

"""
Una planta que fabrica perfiles de hierro posee un lote de n piezas.
Confeccionar un programa que pida ingresar por teclado la cantidad de piezas a procesar y luego ingrese la longitud de cada perfil; sabiendo que la pieza cuya longitud esté comprendida en el rango de 1.20 y 1.30 son aptas. Imprimir por pantalla la cantidad de piezas aptas que hay en el lote.
   
x = 0
y = int(input('Ingrese las piezas a procesar: '))
z = 0
a = 0
b = 0
while x < y:
    b = float(input('Ingresa la longitud de la piezas a procesar: '))
    if b > 1.20 and b < 1.30:
        z += 1
        x += 1
    else :
        a += 1
        x += 1

print('Piezas procesadas bien: ', z)
print('Piezas no procesadas ', a)
"""

""" 
Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.

x = 0
a = 0
b = 0
d = 0

while x < 10:
    d = int(input('Ingrese las notas de los alumnos: '))
    if d >= 7:
        a += 1
        x += 1
    else :
        b += 1
        x += 1
        
print('alumnos con notas mayores a 7 o igual: ', a)
print('Alumnos con notas inferiores a 7: ', b)
        
"""        