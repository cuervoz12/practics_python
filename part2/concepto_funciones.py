"""
Confeccionar una aplicación que muestre una presentación en pantalla del programa. Solicite la carga de dos valores y nos muestre la suma. Mostrar finalmente un mensaje de despedida del programa.
Implementar estas actividades en tres funciones.

def presentacion():

    print(" ------- HOLA A TODOS ------- ")
    print(" ------- PROGRAMA QUE PERMITE INGRESAR DATOS Y SUMARLOS ------- ")
    print(" ******************************* \n")

def sumar_datos ():

    v1 = int(input(" Ingresa el valor 1: "))
    v2 = int(input(" Ingresa el valor 2: "))
    suma = v1 + v2
    print("El valor sumado es: ", suma, "\n")

def finalizar ():

    print(" ------- GRACIAS POR USARLOS ------- ")

presentacion ()
sumar_datos()
finalizar()

"""

"""
Confeccionar una aplicación que solicite la carga de dos valores enteros y muestre su suma.
Repetir la carga e impresion de la suma 5 veces.
Mostrar una línea separadora después de cada vez que cargamos dos valores y su suma.

def sumar_datos ():

    v1 = int(input("Ingresa el valor 1: "))
    v2 = int(input("Ingres el valor 2: "))
    suma = v1 + v2
    print("La suma es: ", suma)

def separar ():

    print("\n-------------------------\n")

for x in range (5):

    sumar_datos()
    separar()

"""

"""
Desarrollar un programa con dos funciones. La primer solicite el ingreso de un entero y muestre el cuadrado de dicho valor. La segunda que solicite la carga de dos valores y muestre el producto de los mismos. LLamar desde el bloque del programa principal a ambas funciones.

def cuadrado ():

    y = int(input("Ingresa un valor para calcular el cuadrado: "))
    cuadrado = y * y
    print(f"El cuadrado del numero {y} es: ", cuadrado, "\n")

def producto ():

    a = int(input("Ingrese un valor para calcular el proudcto: "))
    b = int(input("Ingrese un valor para calcular el proudcto: "))
    productos = a * b
    print(f"EL producto de {a} y {b} es: ", productos, "\n")

cuadrado()
producto()

"""

"""
Desarrollar un programa que solicite la carga de tres valores y muestre el menor. Desde el bloque principal del programa llamar 2 veces a dicha función (sin utilizar una estructura repetitiva)

def menor ():

    a = int(input("Ingresa el valor 1: "))
    b = int(input("Ingresa el valor 2: "))
    c = int(input("Ingresa el valor 3: "))
    if a < b and a < c: 
        print(f"El valor {a} es el menor")
    elif b < a and b < c: 
        print(f"El valor {b} es el menor")
    else: 
        print(f"El valor {c} es el menor")

menor()
menor() 

"""



