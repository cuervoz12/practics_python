"""
Confeccionar una función que reciba un string como parámetro y en forma opcional un segundo string con un caracter. La función debe mostrar el string subrayado con el caracter que indica el segundo parámetro

def titulo_sub (titulo, caracter = "*"):

    print(titulo)
    print(caracter*len(titulo))

titulo_sub ("Sistema de administracion")
titulo_sub ("Ventas", "-")

"""

"""
Confeccionar una función que reciba entre 2 y 5 enteros. La misma nos debe retornar la suma de dichos valores. Debe tener tres parámetros por defecto.

def ingresar_datos (valor1, valor2, valor3 = 0, valor4 = 0, valor5 = 0):

    suma = valor1 + valor2 + valor3 + valor4 + valor5
    return suma

print("suma 1 + 1: ", ingresar_datos(1, 1))
print("suma 1 + 1 + 1: ", ingresar_datos(1, 1, 1))
print("suma 1 + 1 + 1 + 1: ", ingresar_datos(1, 1, 1, 1))
print("suma 1 + 1 + 1 + 1 + 1: ", ingresar_datos(1, 1, 1, 1, 1))

"""

"""
Crea una función saludar() que reciba un nombre con valor por defecto "Juan".

def saludar (saludo, valor = "Juan"):

    print (saludo, valor)

saludar ("Hola")
saludar ("Hola ", "Carlos")

"""

"""
Crea una función sumar(a, b=10) que sume dos números.

def sumar (a, b = 10):

    suma = a + b
    print (suma)

sumar (10)
sumar (10, 5)

"""

"""
Crea una función mostrar_edad(nombre, edad=18) que muestre:

def mostrar_edad (nombre, edad = 18):

    print (nombre, " Tiene ", edad, " años")

mostrar_edad ("Carlos")
mostrar_edad ("Carlos", 20)

"""

"""
Crear una funcion que muestre la potencian de un numero

def potencia (numero, exponente = 2):

    po = numero ** exponente
    print (po)

potencia (2)
potencia (2, 3)

"""

"""
Crear una funcion y para poder ingresar un precio y descuento y mostrar cual seria el descuento

def precio_final (precio, descuento = 10):

    multi = 100 * descuento / 100
    descu = precio - multi
    print ("Descuento: ", descu)

precio_final (100)
precio_final (100, 20)

"""

"""
Crea un funcion que ingrese en el primer parametro un texto y en el segundo cuantas veces se va repetir ese texto

def repetir (valor, veces = 2):

    for x in range (veces):

        print(valor)

repetir ("Hola")
print()
repetir ("Hola", 4)

"""

"""
Crea una funcion que muestre nombre, edad, ciudad para edad y ciudad son parametros por defecto

def persona (nombre, edad = 20, cuidad = "Berlin"):

    print (nombre, " Tiene ", edad, " Es de ", cuidad)

persona ("Andres")
persona ("Jaime", 22, "Medellin")

"""











