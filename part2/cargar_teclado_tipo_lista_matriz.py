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

"""
Se desea saber la temperatura media trimestral de cuatro paises. Para ello se tiene como dato las temperaturas medias mensuales de dichos paises.
Se debe ingresar el nombre del país y seguidamente las tres temperaturas medias mensuales.
Seleccionar las estructuras de datos adecuadas para el almacenamiento de los datos en memoria.
a - Cargar por teclado los nombres de los paises y las temperaturas medias mensuales.
b - Imprimir los nombres de las paises y las temperaturas medias mensuales de las mismas.
c - Calcular la temperatura media trimestral de cada país.
c - Imprimir los nombres de los paises y las temperaturas medias trimestrales.
b - Imprimir el nombre del pais con la temperatura media trimestral mayor.

paises = []
temperaturas = []

for x in range (4):

    p = input("Ingresa el nombre del pais: ")
    paises.append(p)
    temperaturas.append([])

    for y in range (3):
        tem1 = int(input("Ingresa la tempetura  mes: "))
        temperaturas[x].append(tem1)
        
print("\n Paises y sus temperaturas mensuales: \n")

for x in range (4):

    print("\n Pais: ", paises[x])

    for y in range (len(temperaturas[x])):

        print("Temperaturas: ", temperaturas[x][y])

for x in range (4):

    suma = 0
    promedio = 0
    mayor = 0
    pais = paises[0]

    for y in range (len(temperaturas[x])):

        suma += temperaturas[x][y]

    promedio = suma / 3

    print ("\n Pais ", paises[x])
    print("Promedio de temperaturas: ", promedio)

    if promedio > mayor:
        mayor = promedio
        pais = paises[x]

print("\n Pais ", pais)
print("Mayor temperatura trimestral del promedio: ", mayor)

"""

"""
Definir una lista y almacenar los nombres de 3 empleados.
Por otro lado definir otra lista y almacenar en cada elemento una sublista con los números de días del mes que el empleado faltó.
Imprimir los nombres de empleados y los días que faltó.
Mostrar los empleados con la cantidad de inasistencias.
Finalmente mostrar el nombre o los nombres de empleados que faltaron menos días.


empleados = []
faltas = []

for x in range (3):

    e = input("\n Ingresa el nombre del empleado: ")
    empleados.append(e)
    c = int(input("Ingresa la cantidad dias que el empleado falto: "))
    faltas.append([])

    for y in range (c):

        dia = int(input("Ingrese los dias que falto: "))
        faltas[x].append(dia)

for x in range (3):

    print("\n Nombre del empleado: ", empleados[x])

    for y in range (len(faltas[x])):

        print("Dias que falto el empleado: ", faltas[x][y])

for x in range (3):

    cantidad = 0

    cantidad += len(faltas[x])

    print("\n Empleado: ", empleados[x])
    print("Cantidad de faltas: ", cantidad)

    if cantidad < 2: 
        print("Empleado que falto menos de dos dias: ", empleados[x])

"""

"""
Desarrollar un programa que cree una lista de 50 elementos. 
El primer elemento es una lista con un elemento entero, el segundo elemento es una lista de dos elementos etc.

lista = []
cantidad = 1

for x in range (50):

    lista.append([])
    valor = 1

    for y in range (cantidad):

        lista[x].append(valor)
        valor += 1
        
    cantidad +=1

print(lista)

"""


