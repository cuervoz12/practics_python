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

"""
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
    