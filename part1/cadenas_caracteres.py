"""
Realizar la carga del nombre de una persona y luego mostrar el primer caracter del nombre y la cantidad de letras que lo componen.

nombre = input("Ingresa tu nombre: ")

print("El primer caracter del nombre es: ", nombre[0])
print("La cantidade de caracteres es: ", len(nombre))

"""

"""
Solicitar la carga del nombre de una persona en minúsculas. Mostrar un mensaje si comienza con vocal dicho nombre.

nombre = input("Ingresa tu nombre: ")

if nombre[0] == 'a' or nombre[0] == 'e' or nombre[0] == 'i' or nombre[0] == 'o' or nombre[0] == 'u':
    print("El nombre inicia con vocal")
else:
    print("El nombre no inicia con vocal")

"""

"""
Ingresar un mail por teclado. Verificar si el string ingresado contiene solo un caracter "@".

email = input("Ingresa un email: ")
x = 0
cantidad = 0

while x  < len(email):
    
    if email[x] == "@":
        cantidad += 1
    x += 1
    
if  cantidad != 1:
    print("El email contiene mas de dos @")
else: 
    print("El email solo tiene un @")

#### REPARSAR
"""

"""
Inicializar un string con la cadena "mAriA" luego llamar a sus métodos upper(), lower() y capitalize(), guardar los datos retornados en otros string y mostrarlos por pantalla.

nombre = "mAriA"
nombre1 = nombre.upper()
nombre2 = nombre.lower()
nombre3 = nombre.capitalize()

print(nombre1)
print(nombre2)
print(nombre3)

"""

"""
Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se ingresaron. Tener en cuenta que un espacio en blanco es igual a
" ", en cambio una cadena vacía es ""

a = input("Ingresa una oracion ")
x = 0
cantididad = 0

while x < len(a):
    
    if a[x] == " ":
        cantididad += 1
    x += 1

print("la cantidad de espacios son: ", cantididad)

"""

"""
Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas. Contar la cantidad de vocales. Crear un segundo string con toda la oración en minúsculas para que sea más fácil disponer la condición que verifica que es una vocal.

oracion = input("Ingresa una oracion: ")
oracion2 = oracion.lower()
cantidad = 0
x = 0

while x < len(oracion2):
    
    if oracion2[x] == "a" or oracion2[x] == "e" or oracion2[x] == "i" or oracion2[x] == "o" or oracion2[x] == "u":
        cantidad += 1
    x += 1
    
print("Oracion normal: ", oracion)
print("Oracion en miniscula: ", oracion2)
print("Cantidad de vocales: ", cantidad)

"""

"""
Solicitar el ingreso de una clave por teclado y almacenarla en una cadena de caracteres. Controlar que el string ingresado tenga entre 10 y 20 caracteres para que sea válido, en caso contrario mostrar un mensaje de error.

x = True
cantidad = 0

while x == True: 
    
    password = input("Ingrese una clave: ")
    cantidad = len(password)
    
    if cantidad > 10 and cantidad < 20:
        print("Clave ingresada correctamente ")
        x = False

    else: 
        print("Ingresa una clave entre 10 a 20 caracteres ")

"""
