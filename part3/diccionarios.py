"""
productos={"manzanas":39, "peras":32, "lechuga":17}
print(productos)

"""

"""
En el bloque principal del programa definir un diccionario que almacene los nombres de paises como clave y como valor la cantidad de habitantes. Implementar una función para mostrar cada clave y valor.

def imprimir_paises (paises):

    for clave in paises:

        print (clave, paises[clave])

paises={"argentina":40000000, "españa":46000000, "brasil":190000000, "uruguay": 3400000}
imprimir_paises (paises)

"""

"""
Crear un diccionario que permita almacenar 5 artículos, utilizar como clave el nombre de productos y como valor el precio del mismo.
Desarrollar además las funciones de:
1) Imprimir en forma completa el diccionario
2) Imprimir solo los artículos con precio superior a 100.

def cargar_datos ():

    productos = {}

    for x in range (5):

        y = input("Ingresa un producto: ")
        z = int(input("Ingresa el precio: "))
        productos[y] = z
    return productos

def imprimir_todo (productos):

    print()

    for clave in productos:

        print(clave, productos[clave])

def imprimir_mas_cien (productos):

    print()

    for clave in productos:

        if productos[clave] > 100:
            print(clave, productos[clave])

productos = cargar_datos ()
imprimir_todo (productos)
imprimir_mas_cien (productos)

"""

"""
Desarrollar una aplicación que nos permita crear un diccionario ingles/castellano. La clave es la palabra en ingles y el valor es la palabra en castellano.
Crear las siguientes funciones:
1) Cargar el diccionario.
2) Listado completo del diccionario.
3) Ingresar por teclado una palabra en ingles y si existe en el diccionario mostrar su traducción.

def ingresar_datos ():

    palabras = {}

    for x in range (5):

        y = input("Ingresa la palabra en ingles: ")
        z = input("Ingresa la palabra en espanol: ")
        palabras[y] = z
    return palabras

def imprimir_dici (palabras):

    print()
    
    for clave in palabras:

        print (clave, palabras[clave])

def traducir_datos (palabras):

    a = input("\n Ingresa un palabra en ingles a ver si esta en el diccionario: \n")


    if a in palabras:
        print(palabras[a])
    else:
        print("La palabra no tiene su traduccion ")

palabras = ingresar_datos ()
imprimir_dici (palabras)
traducir_datos (palabras)

"""

"""
Crear un diccionario en Python que defina como clave el número de documento de una persona y como valor un string con su nombre.
Desarrollar las siguientes funciones:
1) Cargar por teclado los datos de 4 personas.
2) Listado completo del diccionario.
3) Consulta del nombre de una persona ingresando su número de documento.

def ingresar_datos ():

    personas = {}

    for x in range (4):

        numero = int(input("Ingresa la identificacion de la persona: "))
        nombre = input("Ingresa el nombre de la persona: ")
        personas[numero] = nombre
    return personas

def imprimir_listado (personas):

    print()
    
    for clave in personas:

        print(clave, personas[clave])

def buscar_persona (personas):

    x = int(input("\n Ingresa la identifiacion de la persona: "))

    if x in personas:
        print(personas[x])
    else:
        print("La persona no esta")

personas = ingresar_datos ()
imprimir_listado (personas)
buscar_persona (personas)

"""

