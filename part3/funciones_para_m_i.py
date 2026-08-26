"""
Confeccionar un programa que contenga las siguientes funciones:
1) Carga de una lista y retorno al bloque principal.
2) Fijar en cero todos los elementos de la lista que tengan un valor menor a 10.
3) Imprimir la lista

def cargar_datos ():

    lista = []
    continua = "s"

    while continua == "s":

        y = int(input("Ingresa datos a la lista: "))
        lista.append(y)
        continua = input("Ingresa otra vez la lista: [s/n] ")
    return lista

def cargar_datos_ceros (lista):

    for x in range (len(lista)):

        if lista[x] < 10:
            lista[x] = 0

def imprimir_lista (lista):

    for elemento in lista:

        print(elemento, "-", sep="", end="")
    print("")

lista = cargar_datos ()
print("Lista sin modificar")
imprimir_lista (lista)
print("Lista modificada")
cargar_datos_ceros (lista)
imprimir_lista (lista)

"""

"""
Confeccionar un programa que contenga las siguientes funciones:
1) Carga de una lista de 5 nombres.
2) Ordenar alfabéticamente la lista.
3) Imprimir la lista de nombres

def cargar_datos ():

    lista = []

    for x in range (5):

        y = input("Ingresa el nombre de la persona: ")
        lista.append(y)
    return lista

def ordenar_datos (lista):

    for x in range (4):

        for y in range (4):

            if lista[x] > lista[x+1]:
                aux = lista[x]
                lista[x] = lista[x+1]
                lista[x+1] = aux

def imprimir_datos (lista):

    for x in range (len(lista)):

        print (lista[x]," ",end="")

lista = cargar_datos ()
print("Sin ordenar")
imprimir_datos (lista)
print("\n Ordenado")
ordenar_datos (lista)
imprimir_datos (lista)

"""

"""
Confeccionar un programa que almacene en un diccionario como clave el nombre de un contacto y como valor su número telefónico:
1) Carga de contactos y su número telefónico.
2) Pemitir modificar el número telefónico. Se ingresa el nombre del contacto para su búsqueda.
3) Imprimir la lista completa de contactos con sus números telefónicos.

def carga_datos ():

    contactos = {}
    continua = "s"

    while continua == "s":

        nombre = input("Ingresa el nombre: ")
        telefono = int(input("Ingresa el numero: "))
        contactos[nombre] = telefono
        continua = input("Quieres seguir [s/n]: ")
    return contactos

def modificar_datos (contactos):

    nombre = input("Ingrese el nombre de contacto a modificar el telefono: ")
    if nombre in contactos:
        telefonos = int(input("Ingresa el nuevo numero: "))
        contactos[nombre] = telefonos
    else:
        print("EL numero no existe")

def imprimir_datos (contactos):

    print("Listado de todos los contactos")

    for nombre in contactos:

        print(nombre, contactos[nombre])

lista = carga_datos ()
modificar_datos (lista)
imprimir_datos (lista)

"""

"""
Crear un diccionario en Python para almacenar los datos de empleados de una empresa. La clave será su número de legajo y en su valor almacenar una lista con el nombre, profesión y sueldo.
Desarrollar las siguientes funciones:
1) Carga de datos de empleados.
2) Permitir modificar el sueldo de un empleado. Ingresamos su número de legajo para buscarlo.
3) Mostrar todos los datos de empleados que tienen una profesión de "analista de sistemas"

def cargar():

    empleados={}
    continua="s"

    while continua=="s":
        
        legajo=int(input("Ingrese el numero de legajo:"))
        nombre=input("Ingrese el nombre del empleado:")
        profesion=input("Ingrese el nombre de la profesion:")
        sueldo=float(input("Ingrese el sueldo:"))
        empleados[legajo]=[nombre,profesion,sueldo]
        continua=input("Ingresa los datos de otro empleado[s/n]:")
    return empleados


def imprimir(empleados):

    print("Listado completo de empleados")

    for legajo in empleados:
        print(legajo,empleados[legajo][0],empleados[legajo][1],empleados[legajo][2])


def modificar_sueldo(empleados):

    legajo=int(input("Ingrese el numero de legajo para buscar empleado:"))
    if legajo in empleados:
        sueldo=float(input("Ingrese nuevo sueldo:"))
        empleados[legajo][2]=sueldo
    else:
        print("No existe un empleado con dicho numero de legajo")


def imprimir_analistas(empleados):

    print("Listado de empleados con profesion \"analista de sistemas\"")

    for legajo in empleados:

        if empleados[legajo][1]=="analista de sistemas":
            print(legajo,empleados[legajo][0],empleados[legajo][2])


empleados=cargar()
imprimir(empleados)
modificar_sueldo(empleados)
imprimir(empleados)
imprimir_analistas(empleados)

"""

