"""
Confeccionar un programa que permita cargar un código de producto como clave en un diccionario. Guardar para dicha clave el nombre del producto, su precio y cantidad en stock.
Implementar las siguientes actividades:
1) Carga de datos en el diccionario.
2) Listado completo de productos.
3) Consulta de un producto por su clave, mostrar el nombre, precio y stock.
4) Listado de todos los productos que tengan un stock con valor cero.

def cargar_datos ():

    productos = {}
    continua = "s"

    while continua == "s":

        codigo = int(input("Ingresa el codigo del producto: "))
        descripcion = input("Ingresa la descripcionL: ")
        precio = int(input("Ingresa el precio: "))
        stock = int(input("Ingresa el stock actual: "))
        productos[codigo] = (descripcion, precio, stock)
        continua = input("Quieres seguir agregando otro producto: [s/n]")
        
    return productos

def imprimir_dicci (productos):

    print("\n Lista completa de los productos: ")

    for codigo in productos: 

        print(codigo, productos[codigo][0], productos[codigo][1], productos[codigo][2])

def consulta_dicci (productos):

    codigo = int(input("\n Ingresa el codigo del producto: "))
    if codigo in productos:
        print(codigo, productos[codigo][0], productos[codigo][1], productos[codigo][2])
    else:
        print("El producto no se encuentra")

def productos_valor_cero (productos):

    print()

    for codigo in productos:

        if productos[codigo][2] == 0:
            print(codigo, productos[codigo][0], productos[codigo][1], productos[codigo][2])

productos = cargar_datos ()
imprimir_dicci (productos)
consulta_dicci (productos)
productos_valor_cero (productos)

"""

"""
Confeccionar una agenda. Utilizar un diccionario cuya clave sea la fecha. Permitir almacenar distintas actividades para la misma fecha (se ingresa la hora y la actividad)
Implementar las siguientes funciones:
1) Carga de datos en la agenda.
2) Listado completo de la agenda.
3) Consulta de una fecha.

def cargar_datos ():

    agenda = {}
    continua1 = "s"

    while continua1 == "s":

        fecha = input("Ingresa la fecha en formato: dd/mm/aaaa: ")
        continua2 = "s"
        lista = []

        while continua2 == "s":

            hora = input("Ingresa la hora de la actividad con formato hh:mm : ")
            actividad = input("Ingresa la descripcion de la actividad: ")
            lista.append((hora, actividad))
            continua2 = input("\nQuieres agregar otra actividad a la misma fecha [s/n]: ")
        agenda[fecha] = lista
        continua1 = input("\nQuieres agregar otra actividad a la misma fecha [s/n]: ")
    return agenda

def imprimir_datos (agenda):

    print("\n Listado completa de la agenda")

    for fecha in agenda:

        print ("Para fecha: ", fecha)

        for hora, actividad in agenda[fecha]:

            print(hora, actividad)

def conulta_fecha (agenda):

    fecha = input("\n Ingrese la fecha que desea consultar:")

    if fecha in agenda:

        for hora, actividad in agenda[fecha]:

            print(hora, actividad)
    else:
        print("No se tiene nada agendado")

agenda = cargar_datos ()
imprimir_datos (agenda)
conulta_fecha (agenda)

"""

"""
Se desea almacenar los datos de 3 alumnos. Definir un diccionario cuya clave sea el número de documento del alumno. Como valor almacenar una lista con componentes de tipo tupla donde almacenamos nombre de materia y su nota.
Crear las siguientes funciones:
1) Carga de los alumnos (de cada alumno solicitar su dni y los nombres de las materias y sus notas)
2) Listado de todos los alumnos con sus notas
3) Consulta de un alumno por su dni, mostrar las materias que cursa y sus notas.

def cargar_datos ():

    alumnos = {}
    print()

    for x in range (3):

        ti = int(input("Ingresa la Tarjeta de indentidad del alumno: "))
        lista = []
        continuar = "s"

        while continuar == "s":

            materia = input("Ingresa la materia: ")
            nota = int(input("Ingresa la nota: "))
            lista.append((materia, nota))
            continuar = input("Quieres agregar mas notas o materias: [s/n]")
        alumnos[ti] = lista
    return alumnos

def imprimir_alumnos (alumnos):

    print("\n alumnos ")

    for dni in alumnos:

        print("\n TI del alumno: ", dni)
        print("Materias y notas")
        for materia, nota in alumnos[dni]:

            print(materia, nota)

    print()

def consultar_alumno (alumnos):

    dni = int(input("Ingresa el TI a buscar: "))
    if dni in alumnos:

        for materia, nota in alumnos[dni]:

            print(materia, nota)

alumnos = cargar_datos ()
imprimir_alumnos (alumnos)
consultar_alumno (alumnos)

"""






