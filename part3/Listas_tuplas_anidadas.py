"""
En general podemos crear y combinar tuplas con elementos de tipo lista y viceversa, es decir listas con componente tipo tupla.

empleado = ["Juan", 53, (25, 11, 1999)]
print(empleado)
empleado.append((1, 1, 2016))
print(empleado)
alumno = ("Pedro", [7, 9])
print(alumno)
alumno[1].append(10)
print(alumno)

"""

"""
Almacenar en una lista de 5 elementos tuplas que guarden el nombre de un pais y la cantidad de habitantes.
Definir tres funciones, en la primera cargar la lista, en la segunda imprimirla y en la tercera mostrar el nombre del país con mayor cantidad de habitantes.

def ingresar_datos_paises ():

    paises = []

    for x in range (5):

        y = input("Ingresa el nombre del pais: ")
        z = int(input("Ingresa la cantidad de habitantes: "))
        paises.append((y,z))
    return paises

def imprimir_datos (paises):

    for x in range (5):

        print("Paise: ", paises[x][0], " Habitantes: ", paises[x][1])

def mayor_habitantes (paises):

    pos = 0

    for x in range (5):

        if paises[x][1] > paises[pos][1]:
            pos = 0
    print("Pais con mayor habitantes: ", paises[pos][0])

paises = ingresar_datos_paises ()
imprimir_datos (paises)
mayor_habitantes (paises)

"""
