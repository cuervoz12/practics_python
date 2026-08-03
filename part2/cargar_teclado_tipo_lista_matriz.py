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


