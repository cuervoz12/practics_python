""""
lista1=[0,1,2,3,4,5,6]
lista2=lista1[2:5]
print(lista2) 
lista3=lista1[1:3]
print(lista3) 
lista4=lista1[:3]
print(lista4) 
lista5=lista1[2:]
print(lista5) 

"""

"""
Confeccionar una función que le enviemos un número de mes como parámetro y nos retorne una tupla con todos los nombres de meses que faltan hasta fin de año.

def cargar_datos (datos):

    meses=('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
    return meses[datos:]

print("Imprimir los nombres de los meses que faltan")
datos = int(input("Ingresa el mes en nuemros: "))
meses = cargar_datos (datos)
print(meses)

"""
"""
Confeccionar una función que reciba una cadena de caracteres y nos devuelva los tres primeros.
En el bloque principal del programa definir una tupla con los nombres de meses. Mostrar por pantalla los primeros tres caracteres de cada mes.

def cargar_datos (meses):

    return meses[:3]

meses=('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')

for x in meses:

    print(cargar_datos(x))

"""

"""
Realizar un programa que contenga las siguientes funciones:
1) Carga de una lista de 10 enteros.
2) Recibir una lista y retornar otra con la primer mitad (se sabe que siempre llega una lista con una cantidad par de elementos)
3) Imprimir una lista.

def cargar_datos ():

    lista = []

    for x in range (10):

        y = int(input("Ingresa los datos: "))
        lista.append(y)
    return lista

def cargar_mitad (lista):

    return lista[5:]

lista = cargar_datos ()
print(cargar_mitad (lista))

"""

"""
Cargar una cadena por teclado luego:
1) Imprimir los dos primeros caracteres.
2) Imprimir los dos últimos
3) Imprimir todos menos el primero y el último caracter.

caracter = input("Ingresa una cadena de datos: ")
print(caracter[:2])
print(caracter[len(caracter) - 2:])
print(caracter[1:len(caracter) - 1])

"""



