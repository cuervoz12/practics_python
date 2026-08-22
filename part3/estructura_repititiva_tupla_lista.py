"""
Ahora veremos una segunda forma de acceder a los elementos de una lista con la estructura repetitiva for sin indicar subíndices.


lista=[2, 3, 50, 7, 9]

for elemento in lista:

    print(elemento)

"""

"""
Confeccionar un programa que permita la carga de una lista de 5 enteros por teclado.
Luego en otras funciones:
1) Imprimirla en forma completa.
2) Obtener y mostrar el mayor.
3) Mostrar la suma de todas sus componentes.
Utilizar la nueva sintaxis de for vista en este concepto.

def ingresar_datos ():

    lista = []

    for x in range (5):

        y = int(input("Ingresa un numero entero: "))
        lista.append(y)
    return lista

def imprimir_lista (lista):

    for elemento in lista:

        print(elemento)

def mayor_lista (lista):

    mayor = 0

    for elemento in lista:

        if elemento > mayor:
            mayor = elemento
    print("EL numero mayor es: ", mayor)

def sumar_lista (lista):

    sumar = 0

    for elemento in lista:

        sumar += elemento

    print("La suma total es: ", sumar)

lista = ingresar_datos ()
imprimir_lista (lista)
mayor_lista (lista)
sumar_lista (lista)

"""

"""
Almacenar en una lista de 5 elementos las tuplas con el nombre de empleado y su sueldo.
Implementar las funciones:
1) Carga de empleados.
2) Impresión de los empleados y sus sueldos.
3) Nombre del empleado con sueldo mayor.
4) Cantidad de empleados con sueldo menor a 1000.

def cargar_datos ():

    lista = []

    for x in range (5):

        y = input("Ingresa el nombre del empleado: ")
        z = int(input("Ingresa el sueldo del empleado: "))
        print()
        lista.append((y, z))
    return lista

def imprimir_empleados (lista):

    print("\n Empleados y sus sueldos ")

    for nombre,sueldo in lista:

        print(nombre, sueldo)

def mayor_sueldo (lista):

    mayor = lista[0]

    for empleado in lista:

        if empleado[1] > mayor[1]:
            mayor = empleado
    print("Empleado con mayor sueldo: ", mayor[0], mayor[1])


def sueldos_inferiores (lista):

    cantidad = 0

    for empleado in lista:

        if empleado[1] < 1000:
            cantidad += 1
    print("La cantidad de empleados inferiores a 1000 son: ", cantidad)

lista = cargar_datos ()
imprimir_empleados (lista)
mayor_sueldo (lista)
sueldos_inferiores (lista)

"""


"""
Definir una función que cargue una lista con palabras y la retorne.
Luego otra función tiene que mostrar todas las palabras de la lista que tienen más de 5 caracteres.

def cargar_palabras ():

    lista = []

    for x in range (5):

        y = input("Ingresa la palabra: ")
        lista.append(y)
    return lista


def mas_cinco_palabras (lista):

    print("\n palabra con mas de 5 caracteres")
    for elemento in lista:

        if len(elemento) > 5:
            print(elemento)

lista = cargar_palabras ()
mas_cinco_palabras (lista)

"""

"""
Almacenar los nombres de 5 productos y sus precios. Utilizar una lista y cada elemento una tupla con el nombre y el precio.
Desarrollar las funciones:
1) Cargar por teclado.
2) Listar los productos y precios.
3) Imprimir los productos con precios comprendidos entre 10 y 15.

def cargar_productos ():

    productos = []

    for x in range (5):

        y = input("Ingresa el producto: ")
        z = int(input("Ingesa el precio: "))
        productos.append((y, z))
    return productos

def cargar_imprimir (lista):

    print("\n Productos y precios ")

    for nombre, precio in lista:

        print(nombre, precio)
    print()

def listar_productos (lista):

    print("\n Productos entre 10 y 15")
    for nombre, precio in lista:

        if precio >= 10 and precio <= 15:
            print(nombre, precio)

lista = cargar_productos ()
cargar_imprimir (lista)
listar_productos 

"""

