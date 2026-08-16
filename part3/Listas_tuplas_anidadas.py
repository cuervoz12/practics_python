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

""""
Almacenar en una lista 5 empleados, cada elemento de la lista es una sub lista con el nombre del empleado junto a sus últimos tres sueldos (estos tres valores en una tupla)
El programa debe tener las siguientes funciones:
1)Carga de los nombres de empleados y sus últimos tres sueldos.
2)Imprimir el monto total cobrado por cada empleado.
3)Imprimir los nombres de empleados que tuvieron un ingreso trimestral mayor a 10000 en los últimos tres meses.
Tener en cuenta que la estructura de datos si se carga por asignación debería ser similar a:
empleados = [["juan",(2000,3000,4233)] , ["ana",(3444,1000,5333)] ,  etc.   ]

def ingresar_datos ():

    empleados = []

    for x in range (5):

        nombre = input("Ingresa el nombre del empleado: ")
        suel1 = int(input("Ingresa el primer sueldo: "))
        suel2 = int(input("Ingresa el segundo sueldo: "))
        suel3 = int(input("Ingresa el tercero sueldo: "))
        print()
        empleados.append([nombre, (suel1, suel2, suel3)])
    print(empleados)
    return empleados

def imprimir_monto_total (empleados):

    print()
    print("Monto total en los ultomos 3 meses \n")

    for x in range (5):

        suma = empleados[x][1][0] + empleados[x][1][1] + empleados[x][1][2]
        print(empleados[x][0], suma)
    print()
      
def mayor_sueldo (empleados):

    print("Emepleados mayores a 1000 \n")

    for x in range (5):

        suma = empleados[x][1][0] + empleados[x][1][1] + empleados[x][1][2]
        if suma > 10000:
            print(empleados[x][0], suma)

empleados = ingresar_datos ()
imprimir_monto_total (empleados)
mayor_sueldo (empleados)

"""

"""
Se tiene que cargar los votos obtenidos por tres candidatos a una elección.
En una lista cargar en la primer componente el nombre del candidato y en la segunda componente cargar una lista con componentes de tipo tupla con el nombre de la provincia y la cantidad de votos obtenidos en dicha provincia.
Se deben cargar los datos por teclado, pero si se cargaran por asignación tendría una estructura similar a esta:

candidatos=[ ("juan",[("cordoba",100),("buenos aires",200)]) , ("ana", [("cordoba",55)]) , ("luis", [("buenos aires",20)]) ]
1) Función para cargar todos los candidatos, sus nombres y las provincias con los votos obtenidos.
2) Imprimir el nombre del candidato y la cantidad total de votos obtenidos en todas las provincias.

def ingresar_datos ():

    candidatos = []

    for x in range (3):

        nom = input("Ingresa el nombre del cantididato: ")
        cant = int(input("Ingresa la cantidad de provincias tiene para cargar: "))
        provincias = []

        for y in range (cant):

            ciu = input("Ingresa el nombre de la provincia: ")
            vot = int(input("Ingresa la cantidad de votos de esa provincia: "))
            provincias.append((ciu, vot))
        candidatos.append((nom, provincias))
    return candidatos

def mayores_votos (candidatos):

    for x in range (len(candidatos)):

        suma = 0

        for y in range (len(candidatos[x][1])):

            suma += candidatos[x][1][y][1]
        print(candidatos[x][0], suma)

cantidad = ingresar_datos ()
mayores_votos (cantidad)

"""

