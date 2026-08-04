"""
rear y cargar una lista con los nombres de tres alumnos. Cada alumno tiene dos notas, almacenar las notas en una lista paralela. Cada componente de la lista paralela debe ser también una lista con las dos notas. Imprimir luego cada nombre y sus dos notas.
  
nombres = []
notas = []

for x in range (3):
    
    a = input("Ingresa un nombre: ")
    nombres.append(a)
    no1 = int(input("Ingresa una nota: "))
    no2 = int(input("Ingresa una nota: "))
    notas.append([no1, no2])

for x in range (3):
    
    print("Alumno: ", nombres[x], "sus notas: ", "[ ", notas[x][0], " ] , [ " ,notas[x][1], " ]")  
    
"""

"""
Se tiene que cargar la siguiente información:
· Nombres de 3 empleados
· Ingresos en concepto de sueldo, cobrado por cada empleado, en los últimos 3 meses.
Confeccionar el programa para:

a) Realizar la carga de los nombres de empleados y los tres sueldos por cada empleado.
b) Generar una lista que contenga el ingreso acumulado en sueldos en los últimos 3 meses para cada empleado.
c) Mostrar por pantalla el total pagado en sueldos a cada empleado en los últimos 3 meses
d) Obtener el nombre del empleado que tuvo el mayor ingreso acumulado


nombre = []
sueldos = []
totalsueldos = []

for x in range (3):

    a = input("Ingresa el nombre del empleado: ")
    nombre.append(a)
    s1 = int(input("Ingresa el sueldo 1: "))
    s2 = int(input("Ingresa el sueldo 2: "))
    s3 = int(input("Ingresa el sueldo 3: "))
    sueldos.append([s1, s2, s3])

for x in range (3):

    total = sueldos[x][0] + sueldos[x][1] + sueldos[x][2]
    totalsueldos.append(total)

for x in range (3):

    print("Empleado: ", nombre[x], " Sueldos en los ultimos 3 meses: ", totalsueldos[x])

mayorn = nombre[0]
mayors = totalsueldos[0]

for x in range (1, 3):

    if totalsueldos[x] > mayors:
        mayors = nombre[x]
        mayors = x

print("El empleado con mayor ingreso es: ", mayorn, " con el sueldo: ", mayors) 

"""

"""
Solicitar por teclado dos enteros. El primer valor indica la cantidad de elementos que crearemos en la lista. El segundo valor indica la cantidad de elementos que tendrá cada una de las listas internas a la lista principal.
Mostrar la lista y la suma de todos sus elementos.

lista = []

element = int(input("Ingresa cuantos elementos tendra la lista: "))
subelemnt = int(input("Ingresa elementos que tendra la lista interna: "))

for x in range (element):

    lista.append([])

    for k in range (subelemnt):

        valor = int(input("Ingresa un valor: "))
        lista[x].append(valor)

print(lista)

suma = 0

for x in range (len(lista)):

    for k in range (len(lista[x])):

        suma += lista[x][k]

print("La suma de estos valores es: ", suma)

"""

"""
Definir dos listas de 3 elementos.
La primer lista cada elemento es una sublista con el nombre del padre y la madre de una familia.
La segunda lista está constituida por listas con los nombres de los hijos de cada familia. Puede haber familias sin hijos.
Imprimir los nombres del padre, la madre y sus hijos.
También imprimir solo el nombre del padre y la cantidad de hijos que tiene dicho padre.


padres = []
hijos = []

for x in range (3):

    pa = input("Ingresa el nombre del padre: ")
    ma = input("Ingresa el nombre de la madre: ")
    padres.append([pa, ma])
    cuanto = int(input("Ingresa cuantos hijos tiene la familia: "))
    hijos.append([])

    for y in range (cuanto):

        hijo = input("Ingresa el nombre del hijo: ")
        hijos[x].append(hijo)

print()

for x in range (3):

    print("Padre: ", padres[x][0], " y ", "Madre: ", padres[x][1])

    for y in range (len(hijos[x])):

        print("Hijos: ", hijos[x][y])

print()

for x in range (3):

    print("Padre: ", padres[x][0])
    print("Hijos: ", len(hijos[x]))

"""


