"""
Realizar un  programa que imprima en pantalla los números del 0 al 100. 

for x in range (101):
    print(x)

"""

"""
Realizar un programa que imprima en pantalla los números del 20 al 30.

for x in range (20, 31):
    print (x)

"""

"""
Imprimir todos los números impares que hay entre 1 y 100.

for x in range (100):
    if x % 2 != 0:
        print (x)     

for x in range(1,100,2):
    print(x)

"""

"""
Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre posteriormente la suma de los valores ingresados y su promedio.

suma = 0
promedio = 0

for x in range (10):
    
    y = int(input("Ingresa los valores: "))
    suma += y

promedio = suma/10

print("La suma de los valores es: ", suma)
print("El promedio es: ", promedio)

"""

"""
Escribir un programa que solicite por teclado 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.

mayor = 0
menor = 0

for x in range (10):
    
    y = float(input("Ingrese las notas de los alumnos: "))
    if y >= 7:
        mayor += 1
    else :
        menor += 1

print("Alumnos con notas mayores o iguales a 7: ",mayor)
print("Alumnos con notas menores a 7: ", menor)

"""

"""
Escribir un programa que lea 10 números enteros y luego muestre cuántos valores ingresados fueron múltiplos de 3 y cuántos de 5. Debemos tener en cuenta que hay números que son múltiplos de 3 y de 5 a la vez.

multitres = 0
multicuatro = 0

for x in range (10):
    y = int(input("Ingrese el numero: "))
    if y % 3 == 0:
        multitres += 1
    elif y % 5 == 0:
        multicuatro += 1

print("El numero de multiplos de 3 son: ", multitres)
print("El numero de multiplos de 5 son: ", multicuatro)

"""

"""
Codificar un programa que lea n números enteros y calcule la cantidad de valores mayores o iguales a 1000 (n se carga por teclado)

n = int(input("Ingrese los valores a calcular: "))
mayor = 0

for x in range (n):
    
    y = int(input("Ingrese los valores: "))
    if y >= 1000:
        mayor += 1

print("La cantidad de valores mayores o iguales a 1000 son: ", mayor)

"""

"""
Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida de la base y la altura de un triángulo. El programa deberá informar:
a) De cada triángulo la medida de su base, su altura y su superficie.
b) La cantidad de triángulos cuya superficie es mayor a 12.

n = int(input("Ingrese la cantidad de triangulos a procesar: "))
cantidad = 0

for x in range (n):
    
    if x < n:
        y = int(input("Ingresa la base del triangulo: "))
        z = int(input("Ingresa la altura del triangulo: "))
        superficie = (y * z)/2
         
        print ("altura: ", y)
        print("base: ", z)
        print("Superficie: ", superficie)

        if superficie > 12:
            cantidad += 1

print("los triangulos mayores 12 en superficie son: ", cantidad)

"""

"""
Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los últimos 5 valores ingresados.

suma = 0

for x in range (10):
    
    y = int(input("Ingresa un valor: "))
    if x > 4:
        suma += y
        
print("la suma de los ultimos valores es: ", suma)

"""  

"""  
Desarrollar un  programa que muestre la tabla de multiplicar del 5 (del 5 al 50)

for x in range (1,51):
    print (5, " * ", x , " = ", 5*x)
    
"""  

""" 
Confeccionar un programa que permita ingresar un valor del 1 al 10 y nos muestre la tabla de multiplicar del mismo (los primeros 12 términos)
Ejemplo: Si ingreso 3 deberá aparecer en pantalla los valores 3, 6, 9, hasta el 36.

y = int(input("Ingresa un valor para mostrar la tabla de multiplicar "))

for x in range (1,13):
    print (y, " * ",x," = ", y*x)    
    
""" 

""" 
Realizar un programa que lea los lados de n triángulos, e informar:
a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
b) Cantidad de triángulos de cada tipo.

a = int(int(input("Ingresa la cantidad de triangulos a procesar: ")))
equi = 0
isos = 0
esca = 0

for x in range (a):
    
    b = int(input("Ingresa 1 lado: "))
    c = int(input("Ingresa 2 lado: "))
    d = int(input("Ingresa 3 lado: "))
    
    if b == c and d == b and c == d:
        print("Triangulo es equilatero ")
        equi += 1
    elif b != c and d != b and c != d:
        print("Triangulo es escaleno")
        esca += 1
    else: 
        print("Trinagulo es isoseles")
        isos += 1

print("Cantidad de equilateros es: ", equi)
print("Cantidad de isoseles es: ", isos)
print("Cantidad de escaleno es: ", esca)

"""  

"""  
Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano.
Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante. Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.

a = int(input("Ingrese los puntos a procesar: "))

uno = 0
dos = 0
tres = 0
cuatro = 0

for x in range (a):
    
    b = int(input("Ingresa el punto para x: "))
    c = int(input("Ingresa el punto para y: "))
    print("")
    
    if b > 0 and c > 0:
        uno += 1
    elif b > 0 and c < 0:
        dos += 1
    elif b < 0 and c < 0:
        tres += 1
    elif b < 0 and c > 0:
        cuatro += 1

print("Puntos ingresados en el cuadrante 1: ", uno)
print("Puntos ingresados en el cuadrante 2: ", dos)
print("Puntos ingresados en el cuadrante 3: ", tres)
print("Puntos ingresados en el cuadrante 4: ", cuatro)

"""  

"""  
Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
a) La cantidad de valores ingresados negativos.
b) La cantidad de valores ingresados positivos.
c) La cantidad de múltiplos de 15.
d) El valor acumulado de los números ingresados que son pares.

negativos = 0
positivos = 0
multipos = 0
acumulado = 0

for x in range (10):
    y = int(input("Ingrese los valores: "))
    
    if y < 0:
        negativos += 1
    elif y % 15 == 0:
        multipos += 1
    elif y % 2 == 0:
        acumulado += y
    else: 
        positivos += 1

print(" Numeros negativos: ", negativos)
print(" Numeros positivos: ", positivos)
print(" Numeros multiplos de 15: ", multipos)
print(" Numeros acumulados que sean pares: ", acumulado)

"""  

"""  
Se cuenta con la siguiente información:
Las edades de 5 estudiantes del turno mañana.
Las edades de 6 estudiantes del turno tarde.
Las edades de 11 estudiantes del turno noche.
Las edades de cada estudiante deben ingresarse por teclado.
a) Obtener el promedio de las edades de cada turno (tres promedios)
b) Imprimir dichos promedios (promedio de cada turno)
c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor.

manana = 0
tarde = 0
noche = 0

promedio1 = 0
promedio2 = 0
promedio3 = 0

for x in range (1, 23):
    
    if x < 6:
        a = int(input("Ingresa la edad de los estudiantes de la manana: "))
        manana += a
    elif x < 12:
        b = int(input("Ingresa la edad de los estudiantes de la tarde: "))
        tarde += b
    elif x < 23:
        c = int(input("Ingresa la edad de los erstudiantes de la noche: "))
        noche += c
        
promedio1 = manana / 22
promedio2 = tarde / 22
promedio3 = noche / 22

if promedio1 > promedio2 and promedio1 > promedio3:
    print("el promedio mayor de edad es en la manana")
elif promedio2 > promedio1 and promedio2 > promedio3:
    print("el promedio mayor de edad es en la tarde")
elif promedio3 > promedio1 and promedio3 > promedio2:
    print("el promedio mayor de edad es en la noche")
else:
    print("El promedio es igual")

print("promedio manana: ", manana)
print("promedio tarde: ", tarde)
print("promedio noche: ", noche)

"""  


        
