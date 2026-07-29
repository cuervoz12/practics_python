"""
Desarrollar un  programa que permita cargar 5 nombres de personas y sus edades respectivas. Luego de realizar la carga por  teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años) 

nombre = []
edad = []
mayores = []

for x in range (5):
    
    a = input("Ingresa el nombre de la persona: ")
    nombre.append(a)
    b = int(input("Ingresa la edad de la persona: "))
    edad.append(b)
    if edad[x] >= 18:
        mayores.append(a)

print(nombre)
print(edad)
print("personas mayores iguales a 18: ", mayores)
    
"""

"""
Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos precios en otra. Definir dos listas paralelas. Mostrar cuantos productos tienen un precio mayor al primer producto ingresado.

producto = []
precio = []
productos = []
for x in range (5):
    a = input("Ingresa el producto: ")
    producto.append(a)
    b = int(input("Ingresa el precio del producto: "))
    precio.append(b)
    
    menor = precio[0]
    
    if precio[x] > menor:
        menor = precio[x]
        productos.append(a)

print(producto)
print(precio)
print("productos mas caros que el primer producto ingresadp: ", productos)

"""

"""
En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben procesar de acuerdo a lo siguiente:
a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)
b) Realizar un listado que muestre los nombres, notas y condición del alumno. En la condición, colocar "Muy Bueno" si la nota es mayor o igual a 8, "Bueno" si la nota está entre 4 y 7, y colocar "Insuficiente" si la nota es inferior a 4.
c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”.

alumno = []
nota = []
cantidad = 0

for x in range (4):
    
    a = input("Ingresa el nombre del alumno: ")
    alumno.append(a)
    b = float(input("Ingresa la nota del alumno: "))
    nota.append(b)
    
for x in range (4):
    
    print(alumno[x])
    print(nota[x])
    if nota[x] >= 8:
        print("Muy bueno")
        cantidad += 1
    elif nota[x] >= 4 and nota[x] <= 7:
        print("Bueno")
    else:
        print("Insuficiente")

print("cantidad de alumnos con muy bueno", cantidad)

"""
 
"""
Realizar un programa que pida la carga de dos listas numéricas enteras de 4 elementos cada una. Generar una tercer lista que surja de la suma de los elementos de la misma posición de cada lista. Mostrar esta tercer lista.

listauno = []
listados = []
listatres = []

for x in range (4):
    
    a = int(input("Ingresa un numero para lista 1: "))
    listauno.append(a)
    b = int(input("Ingresa un numero para lista 2: "))
    listados.append(b)
    
    if listauno[x] == listados[x]:
        listatres.append(a+b)

print(listauno)
print(listados) 
print("suma de la posicion de la lista")
print(listatres)    

"""



   