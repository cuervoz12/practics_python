"""
Definir por asignación una lista de enteros en el bloque principal del programa. Elaborar tres funciones, la primera recibe la lista y retorna la suma de todos sus elementos, la segunda recibe la lista y retorna el mayor valor y la última recibe la lista y retorna el menor.

def sumar_lista (lista):

    suma = 0

    for x in range (len(lista)):

        suma += lista[x]
    return suma 

def mayor_lista (lista):

    mayor = lista[0]

    for x in range (len(lista)):

        if lista[x] > mayor:
            mayor = lista[x]

    return mayor

def menor_lista (lista):

    menor = lista[0]

    for x in range(len(lista)):

        if lista[x] < menor:
            menor = lista[x]
    return menor

def principal ():

    listav = [1, 5, 2, 3, 4]
    print ("la suma de los valores de la lista es: ", sumar_lista(listav), "\n")
    print("El numero mayor de la lista es: ", mayor_lista(listav), "\n")
    print("El numero menor de la lista es: ", menor_lista(listav), "\n")

principal()

"""

"""
Crear y cargar por teclado en el bloque principal del programa una lista de 5 enteros. Implementar una función que imprima el mayor y el menor valor de la lista.

def mayor_menor_lista (lista):

    mayor = lista[0]
    menor = lista[0]

    for x in range (len(lista)):

        if lista[x] > mayor:
            mayor = lista[x]
        if lista[x] < menor:
            menor = lista[x]
    print("El numero mayor es: ", mayor)
    print("EL numero menor es: ", menor)

def principal ():

    listav = []

    for x in range (5):

        y =int(input("Ingresa los valores: "))
        listav.append(y)

    print()
    print(listav)
    mayor_menor_lista (listav)

principal ()

"""

"""
Crear una lista de enteros por asignación. Definir una función que reciba una lista de enteros y un segundo parámetro de tipo entero. Dentro de la función mostrar cada elemento de la lista multiplicado por el valor entero enviado.

def multiplicar (lista, valor):

    listan = []
    for x in range (len(lista)):

        v = lista[x] * valor
        listan.append(v)

    print(listan)

def principal ():

    lista=[3, 7, 8, 10, 2]
    print(lista)
    multiplicar (lista, 3)
    

principal ()

"""

"""
Desarrollar una función que reciba una lista de string y nos retorne el que tiene más caracteres. Si hay más de uno con dicha cantidad de caracteres debe retornar el que tiene un valor de componente más baja.

def mas_caracteres (lista):

    pos = 0

    for x in range (1, len(lista)):

        if len(lista[x]) > len(lista[pos]):
            pos = x

    return lista[pos]

palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print("Palabra mas caracteres: ", mas_caracteres(palabras))

"""

"""
Definir una lista de enteros por asignación en el bloque principal. Llamar a una función que reciba la lista y nos retorne el producto de todos sus elementos. Mostrar dicho producto en el bloque principal de nuestro programa.

def producto (lista):

    producto = 1

    for x in range (len(lista)):

        producto = producto * lista[x]
    return producto

lista = [2, 3, 4, 5]
print(lista)
print("El producto: ", producto(lista))

"""



