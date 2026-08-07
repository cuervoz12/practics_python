"""
Crear una lista por asignación con 5 enteros. Eliminar el primero, el tercero y el último de la lista.

lista=[10, 20, 30, 40, 50]
lista.pop(0)
lista.pop(1)
lista.pop(2)
print(lista)

"""

"""
Crear una lista y almacenar 10 enteros pedidos por teclado. Eliminar todos los elementos que sean iguales al número entero 5.

lista = []

for x in range (10):

    y = int(input("Ingresa datos a la lista: "))
    lista.append(y)

print(lista)
print()

z = 0

while z < len(lista):

    if lista[z] ==5:
        lista.pop(z)
    else:
        z += 1

print(lista)

"""

"""
Crear dos listas paralelas. En la primera ingresar los nombres de empleados y en la segunda los sueldos de cada empleado.
Ingresar por teclado cuando inicia el programa la cantidad de empleados de la empresa.
Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el sueldo como su nombre)

empleados = []
sueldos  = []

e = int(input("Ingresa la cantidad de empleados: "))

for x in range (e):

    n = input("Ingresa el nombre del empleado: ")
    empleados.append(n)
    s = int(input("Ingresa el sueldo del empleado: "))
    sueldos.append(s)

y = 0
print("\n Empleados y sus sueldos ")
print(empleados)
print(sueldos, "\n")

while y < len(sueldos):

    if sueldos[y] > 10000:
        empleados.pop(y)
        sueldos.pop(y)
    else:
        y += 1

print("Empleados y sus sueldos ")
print(empleados)
print(sueldos)

"""

"""
Crear una lista de 5 enteros y cargarlos por teclado. Borrar los elementos mayores o iguales a 10 y generar 
una nueva lista con dichos valores.


lista = []
listados = []

for x in range (5):

    y = int(input("Ingresa un numero: "))
    lista.append(y)

print()
print(lista)
print()
z = 0

while z < len(lista):

    if lista[z] >= 10:
        listados.append(lista[z])
    if lista[z] >= 10:
        lista.pop(z)
    else:
        z += 1

print(lista)
print(listados)

"""



