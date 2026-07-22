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

"""  
Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas

x = 0
suma = 0
promedio = 0
y = int(input("Ingresa el numero de personas para sacar el promedio: "))

while x < y :
    z = float(input("Ingresa la alutra de las personas: "))
    suma += z
    x += 1

promedio = suma/y
print (" el promedio de la alturas es: ", promedio)

"""  

"""  
En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.

a = 0
b = int(input("Ingresa la cantidad de empleados que estan en la empresa: "))
menor = 0
mayor = 0
suma = 0

while a < b: 
    c = int(input("Ingresa el salario del empleado: "))
    if c >= 100 and c <= 300:
        menor += 1
    elif c > 300:
        mayor += 1
    else: 
        print("valor no permitido")
    a += 1
    suma += c

print ("cantidad de empleados que ganan entre 100 y 300: ", menor)
print ("cantidad de empleados que ganan mas de 300: ", mayor)
print("sueldo que gasta la empresa pagando: ", suma)    


"""  

"""  
Realizar un programa que imprima 25 términos de la serie 11 - 22 - 33 - 44, etc. (No se ingresan valores por teclado

x = 0
y =0

while x < 25:
    y +=11
    x += 1
    print(y)
    
"""

"""
Mostrar los múltiplos de 8 hasta el valor 500. Debe aparecer en pantalla 8 - 16 - 24, etc

x = 0
y = 0
z = 0

while x < 500:
    z += 1
    y = 8 * z
    x += 1
    print (y)

"""

"""
Realizar un programa que permita cargar dos listas de 15 valores cada una. Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.

a = 0
b = 0

lista1 = 0
lista2 = 0
iguales = 0

while a < 15:
    c = int(input("ingresa un valor para la lista 1: "))
    lista1 += c
    a += 1

while b < 15:
    d = int(input("ingresa un valor para la lista 2: "))
    lista2 += d
    b += 1
    
if lista1 > lista2:
    print("Lista 1 mayor")
elif lista2 > lista1:
    print("Lista 2 mayor")    
else: 
    print("Son iguales")

"""

"""
Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos valores fueron pares y cuántos impares.
Emplear el operador “%” en la condición de la estructura condicional (este operador retorna el resto de la división de dos valores, por ejemplo 11%2 retorna un 1):

x = 0
y = int(input("Ingrese la cantidad a calcular: "))

pares = 0
impares = 0

while x < y:
    z = int(input("Ingrese un numero: "))
    
    if z % 2 == 0 :
        pares += 1
    else: 
        impares += 1 
    x += 1
    
print("los numeros pares son: ", pares)
print("los numeros impares son: ", impares)

"""
