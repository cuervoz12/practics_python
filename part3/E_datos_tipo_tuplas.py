"""
Definir varias tuplas e imprimir sus elementos.

tupla = (1, 2, 3)
fecha = (20, "Diciembre", 2016)
punto = (10, 2)
persona = ("Rodriguez", "Pablo", 20)

print(tupla)
print(fecha)
print(punto)
print(persona)

""" 

"""
Desarrollar una función que solicite la carga del dia, mes y año y almacene dichos datos en una tupla que luego debe retornar. La segunda función a implementar debe recibir una tupla con la fecha y mostrarla por pantalla.

def ingresar_fecha ():

    dia = int(input("Ingresa el dia: "))
    mes = int(input("Ingresa el mes: "))
    year = int(input("Ingresa el year: "))
    return (dia, mes, year)

def imprimir_fecha (fecha):

    print ("Dia: ", fecha[0], " Mes: ", fecha[1], " Year: ",fecha[2])

fecha = ingresar_fecha ()
imprimir_fecha (fecha)

"""

"""
Definir una tupla con tres valores enteros. Convertir el contenido de la tupla a tipo lista. Modificar la lista y luego convertir la lista en tupla.

tupla1 = (1, 2, 3)
lista = []
tupla2 = ()
def convertir_lista (tupla):

    for x in range (3):

        lista.append(tupla[x])
    print(lista)
    print()

    for x in range (3):

        if lista[x] >= 3:
            lista[x] = 4
    print (lista)
    print()

def convertir_tupla (lista):

    tupla2 = tuple(lista)
    print(tupla2)
            
convertir_lista (tupla1)
convertir_tupla (lista)

"""

"""
Confeccionar un programa con las siguientes funciones:
1)Cargar una lista de 5 enteros.
2)Retornar el mayor y menor valor de la lista mediante una tupla.
Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor.

lista = []

def ingresar_datos ():

    for x in range (5):

        y = int(input("Ingresa los datos: "))
        lista.append(y)
    print(lista)
    print()

def mayor_menor_tupla (lista):

    mayor = lista[0]
    menor = lista[0]

    for x in range (len(lista)):

        if lista[x] > mayor:
            mayor = lista[x]
        if lista[x] < menor:
            menor = lista[x]
    return mayor, menor

ingresar_datos ()
mayor, menor = mayor_menor_tupla (lista)
print("El numero mayor es: ", mayor)
print("El numero menor es: ", menor)

"""

"""
Confeccionar un programa con las siguientes funciones:
1)Cargar el nombre de un empleado y su sueldo. Retornar una tupla con dichos valores
2)Una función que reciba como parámetro dos tuplas con los nombres y sueldos de empleados y muestre el nombre del empleado con sueldo mayor.
En el bloque principal del programa llamar dos veces a la función de carga y seguidamente llamar a la función que muestra el nombre de empleado con sueldo mayor.

def empleados_datos ():

    x = input("Ingresa el nombre del empleados: ")
    y = int(input("Ingresa el sueldo del empleado: "))
    return x, y

def mayor_sueldos (empleado1, empleado2):

    if empleado1[1] > empleado2[1]:
        print(f"EL empleado: {empleado1[0]} tiene mayor sueldo ")
    else:
        print(f"EL empleado: {empleado2[0]} tiene mayor sueldo ")

empleado1 = empleados_datos ()
empleado2 = empleados_datos ()
mayor_sueldos (empleado1, empleado2)

"""

