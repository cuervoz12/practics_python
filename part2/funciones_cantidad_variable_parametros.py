"""
Confeccionar una función que reciba entre 2 y n (siendo n = 2,3,4,5,6 etc.) valores enteros, retornar la suma de dichos parámetros.

def sumar (valor, valor2, *numeros):

    suma = valor + valor2

    for x in range (len(numeros)):

        suma += numeros[x]
    return suma

print("Suma 1 + 1")
print(sumar (1, 1))
print("Suma 1 + 1 + 1")
print(sumar (1, 1, 1))
print("Suma 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1")
print (sumar (1, 1, 1,1, 1, 1,1, 1, 1, 1))

"""

"""
Desempaquetar una lista o tupla
Puede ser que tengamos una función que recibe una cantidad fija de parámetros y necesitemos llamarla enviando valores que se encuentran en una lista o tupla. La forma más sencilla es anteceder el caracter * al nombre de la variable:

def sumar (v1, v2, v3):

    return v1 + v2 + v3

lista = [2, 4, 5]
suma = sumar (*lista)
print(suma)

"""

"""
Confeccionar una función que reciba una serie de edades y me retorne la cantidad que son mayores o iguales a 18 (como mínimo se envía un entero a la función)

def edades_datos (ed1, *ed2):

    cantidad = 0

    if ed1 >= 18:
        cantidad += 1

    for x in range (len(ed2)):

        if ed2[x] >= 18:
            cantidad += 1
    return cantidad

print ("La cantidad de personas mayores o iguales a 18 son: ", edades_datos(1, 2, 3, 18, 19, 20, 7, 8, 9, 10))

"""



