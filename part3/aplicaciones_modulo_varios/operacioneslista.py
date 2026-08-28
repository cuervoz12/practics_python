def cargar_datos ():

    lista = []
    y = int(input("Ingresa la longitud de la lista: "))

    for x in range (y):

        z = int(input("Ingresa los datos: "))
        lista.append(z)
    return lista

def indentificar_mayor (lista):

    mayor = lista[0]

    for x in range (len(lista)):

        if lista[x] > mayor:
            mayor = lista[x]
    return mayor

def sumar_lista (lista):

    suma = 0

    for x in range (len(lista)):

        suma += lista[x]
    return suma


