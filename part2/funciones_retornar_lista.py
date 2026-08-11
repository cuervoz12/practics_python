"""
Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne. Una segunda función debe recibir una lista y mostrar todos los valores mayores a 10. Desde el bloque principal del programa llamar a ambas funciones.

def ingresar_datos ():

    lista = []

    for x in range (5):

        y = int(input("Ingresar un dato entero: "))
        lista.append(y)
    return lista

def mayores (lista):

    listam = []

    for x in range (5):

        if lista[x] > 10: 
            listam.append(lista[x])

    print("\n Los datos mayores a 10 son: ", "\n", listam)

lista = ingresar_datos ()
mayores (lista)

"""

"""
Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne. Una segunda función debe recibir una lista y retornar el mayor y el menor valor de la lista. Desde el bloque principal del programa llamar a ambas funciones e imprimir el mayor y el menor de la lista.

def ingresar_datos ():

    lista = []

    for x in range (5):

        y = int(input("Ingresa los datos: "))
        lista.append(y)
    return lista

def lista_m_m (lista):

    mayor = lista[0]
    menor = lista[0]

    for x in range (5):

        if lista[x] > mayor:
            mayor = lista[x]
        if lista[x] < menor:
            menor = lista[x]
    return [mayor, menor]

lista = ingresar_datos ()
retornar = lista_m_m (lista)
print("El numero mayor es: ", retornar[0])
print("El numenor menor es: ", retornar[1])

"""

"""
Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas. Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años)
Imprimir la edad promedio de las personas.

def ingresar_datos ():

    nombres= []
    edades = []

    for x in range (5):

        a = input("Ingresar el nombre de la persona: ")
        nombres.append(a)
        b = int(input("Ingresa la edad de la persona: "))
        edades.append(b)

    return [nombres, edades]

def mayores (nombres, edades):

    print("\n Peronas mayores: ")

    for x in range (len(nombres)):

        if edades[x] >= 18:
            print("nombre: ", nombres[x])

def promedio (edades):

    suma = 0

    for x in range (len(edades)):

        suma += edades[x]

    promedio = suma / 5
    print("Promedio de edades: ", promedio)

nombre, edade  = ingresar_datos ()
mayores (nombre, edade)
promedio (edade)

"""

"""
En una empresa se almacenaron los sueldos de 10 personas.
Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
1) Carga de los sueldos en una lista.
2) Impresión de todos los sueldos.
3) Cuántos tienen un sueldo superior a $4000.
4) Retornar el promedio de los sueldos.
5) Mostrar todos los sueldos que están por debajo del promedio.

def ingresar_datos ():

    sueldos = []

    for x in range (10):

        y = int(input("Ingresa el sueldo de la persona: "))
        sueldos.append(y)
    return sueldos

def imprimir (sueldos):

    print("Los sueldos son: ")
    print(sueldos)

def mayor (sueldos):

    suma = 0

    for x in range (len(sueldos)):

        if sueldos[x] > 4000:
            suma += 1
    print("la cantidad de sueldos superiores a 4 mil son: ", suma)

def promedio (sueldos):

    suma = 0
    
    for x in range (len(sueldos)):

        suma += sueldos[x]
    promedio = suma / len(sueldos)
    return promedio

def menores (sueldos):

    pro = promedio(sueldos)
    print("Los sueldos inferirores a 4 mil: ")
    print("Promedio: ", pro)
    for x in range (len(sueldos)):

        if sueldos[x] < pro:
            print(sueldos[x])

ingresar_valores = ingresar_datos ()
imprimir_datos = imprimir (ingresar_valores)
mayores_datos = mayor (ingresar_valores)
promedio_valores = promedio (ingresar_valores)
menores_datos = menores(ingresar_valores)

"""

"""
Desarrollar una aplicación que permita ingresar por teclado los nombres de 5 artículos y sus precios.
Definir las siguientes funciones:
1) Cargar los nombres de articulos y sus precios.
2) Imprimir los nombres y precios.
3) Imprimir el nombre de artículo con un precio mayor
4) Ingresar por teclado un importe y luego mostrar todos los artículos con un precio menor igual al valor ingresado.

def ingresar_datos ():

    articulos = []
    precios = []

    for x in range (5):

        a = input("Ingrese un articulo: ")
        articulos.append(a)
        b = int(input("Ingrese el precio: "))
        precios.append(b)

    return [articulos, precios]

def imprimir (articulos, precios):

    print("\n Articulos y precios: ")
    print(articulos)
    print(precios)

def mayor_articulo (articulos, precios):

    mayor = precios[0]
    mayora = articulos[0]

    for x in range (5):

        if precios[x] > mayor:
            mayor = precios[x]
            mayora = articulos[x]
    print(f"\nEl articulo con mayor precio es {mayora} con precio {mayor}")

def comprar (articulos, precios):

    y = int(input("\nIngrese el precio de un articulo para saber aritulos con precio menor: "))

    for x in range (len(precios)):

        if precios[x] < y:

            print(f"\nArticulo {articulos[x]} precios {precios[x]}")

articulos, precios = ingresar_datos ()
imprimir (articulos, precios)
mayor_articulo (articulos, precios)
comprar (articulos, precios)

"""

"""
Confeccionar un programa que permita:
1) Cargar una lista de 10 elementos enteros.
2) Generar dos listas a partir de la primera. En una guardar los valores positivos y en otra los negativos.
3) Imprimir las dos listas generadas.

def datos_ingresados ():

    lista = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]
    return lista

def negativos_positivos (lista):

    listap = []
    listan = []

    for x in range (10):
        
        if lista[x] < 0:
            listan.append(lista[x])
        else:
            listap.append(lista[x])
    print(listap)
    print(listan)

lista = datos_ingresados ()
negativos_positivos (lista)

"""

