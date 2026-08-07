"""
Confeccionar una aplicación que muestre una presentación en pantalla del programa. Solicite la carga de dos valores y nos muestre la suma. Mostrar finalmente un mensaje de despedida del programa.

def presentacion (mensaje):

    print("***************")
    print(mensaje)
    print("*************** \n")

def sumar_datos (n1, n2):

    suma = n1 + n2
    print("La suma es: ", suma, "\n")

presentacion ("HOLA SON PARAMETROS")
sumar_datos(2, 2)

"""

"""
Confeccionar una función que reciba tres enteros y nos muestre el mayor de ellos. La carga de los valores hacerlo por teclado.

def calcular_valores (v1, v2, v3):

    if v1 > v2 and v1 > v3:
        print("El valor mayor es: ", v1)
    elif v2 > v1 and v2 > v3:
        print("El valor mayor es: ", v2)
    else: 
        print("El valor mayor es: ", v3)

def cargar_datos ():

    va1 = int(input("Ingresa el valor 1: "))
    va2 = int(input("Ingresa el valor 2: "))
    va3 = int(input("Ingresa el valor 3: "))
    calcular_valores (va1, va2, va3)

cargar_datos ()

"""

"""
Desarrollar un programa que permita ingresar el lado de un cuadrado. Luego preguntar si quiere calcular y mostrar su perímetro o su superficie.

def cuadrado_dato (v1):

    print("Quieres ver el perimetro o la superficie del cuadrado")
    
    y = int(input("\n.1 para superficie \n.2 para perimetro \nIngresa el numero: "))
    if y == 1:
        superficie = v1 * v1
        print("La superfice es: ", superficie)
    if y == 2: 
        perimetro = v1 * 4
        print("El perimetro es: ", perimetro)

def ingregar_datos():

    x = int(input("Ingresa un valor a calcular: "))
    cuadrado_dato (x)

ingregar_datos ()

"""

"""
Desarrollar una funcion que reciba un string como parametro y nos muestre la cantidad de vocales. Llamarla desde el bloque principal del programa 3 veces con string distintos.

def cantidad_vo (parametro):

    cantidad = 0
    for x in range (len(parametro)):

        if parametro[x] == "a" or parametro[x] == "e" or parametro[x] == "i" or parametro[x] == "o" or parametro[x] == "u":
            cantidad += 1
    print ("Cantidad de vocales es: ", cantidad)

def ingresar ():

    for x in range (3):

        y = input("\n Ingresa la palabra que quieras ingresarle vocales: ")
        cantidad_vo(y)

ingresar()

"""

"""
Confeccionar una función que reciba tres enteros y los muestre ordenados de menor a mayor. En otra función solicitar la carga de 3 enteros por teclado y proceder a llamar a la primer función definida.

def menor_a_mayor (v1, v2, v3):

    lista = [v1, v2, v3]

    print("Lista sin ordenar: ")
    print(lista)
    print()

    lista.sort()

    print("Lista de menor a mayor: ")
    print(lista)
    print()

def ingresar_datos ():

    va1 = int(input("Ingresa el valor 1: "))       
    va2 = int(input("Ingresa el valor 2: "))
    va3 = int(input("Ingresa el valor 3: "))

    menor_a_mayor (va1, va2, va3)

ingresar_datos()

"""



