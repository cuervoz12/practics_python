"""
Confeccionar una función que le enviemos como parámetro el valor del lado de un cuadrado y nos retorne su superficie.

def envari_parametro (valor):

    sup = valor * valor
    return sup

y = int(input("Ingresa el valor: "))
superficie = envari_parametro(y)

print("EL valor de la superfice del cuadrado es: ", superficie)

"""

"""
Confeccionar una función que le enviemos como parámetros dos enteros y nos retorne el mayor.

def ingresar_valores (v1, v2):

    if v1 > v2:
        return v1
    else:
        return v2

x = int(input("Ingresa el valor 1: "))
y = int(input("Ingresa el valor 2: "))

mayor = ingresar_valores (x, y)

print("El valor mayor es: ", mayor)

"""

"""
Confeccionar una función que le enviemos como parámetro un string y nos retorne la cantidad de caracteres que tiene. En el bloque principal solicitar la carga de dos nombres por teclado y llamar a la función dos veces. Imprimir en el bloque principal cual de las dos palabras tiene más caracteres.

def parametros_string (valor):

    return len(valor)

def principal ():

    x = input("Ingresa una palabra: ")
    y = input("Ingresa otra palabra: ")
    valor1 = parametros_string(x)
    valor2 = parametros_string(y)
    if valor1 > valor2:
        print("La palabra con mayor mas caracteres es: ", x)
    elif valor2 > valor1: 
        print("La palabra con mayor mas caracteres es: ", y)
    else:
        print("Tiene los mismo caracteres")
        
principal()

"""

""""
Elaborar una función que reciba tres enteros y nos retorne el valor promedio de los mismos.

def ingresar_datos (v1, v2, v3):

    pro = (v1 + v2 + v3)/3
    return pro

valor1 = int(input("Ingresa valor 1: "))
valor2 = int(input("Ingresa valor 2: "))
valor3 = int(input("Ingresa valor 3: "))

resultado = ingresar_datos(valor1, valor2, valor3)

print("El promedio de los mismo es: ", resultado)

"""

"""
Elaborar una función que nos retorne el perímetro de un cuadrado pasando como parámetros el valor de un lado.

def ingresar_valor (valor): 

    per = valor * 4
    return per

y = int(input("Ingresa un valor para calcular el perimetro: "))
resultado = ingresar_valor(y)
print("El perimetro es: ", resultado)

"""

"""
Confeccionar una función que calcule la superficie de un rectángulo y la retorne, la función recibe como parámetros los valores de dos de sus lados:

def ingresar_valor (lado1, lado2):

    su = lado2 * lado1
    return su

x = int(input("Ingresa altura del rectangulo: "))
y = int(input("Ingresa base del rectangulo: "))

resutlado = ingresar_valor(x, y)

print("La superficie del rectangulo es: ", resutlado)

"""

"""
En el bloque principal del programa cargar los lados de dos rectángulos y luego mostrar cual de los dos tiene una superficie mayor.

def ingresar_valores (v1, v2, v3, v4):

    sup1 = v1 * v2
    sup2 = v3 * v4

    if sup1 > sup2:
        print("el rectangulo mayor es 1")
        return sup1
    elif sup2 > sup1:
        print("el rectangulo mayor es 2")
        return sup2
    else:
        print("Son iguales")

def principal ():

    a = int(input("Ingresa la base para el rectangulo 1: "))
    b = int(input("Ingresa la altura para el rectangulo 1: "))
    c = int(input("Ingresa la base para el rectangulo 2: "))
    d = int(input("Ingresa la altura para el rectangulo 2: "))
    datos = ingresar_valores(a, b, c, d)

    print(datos)

principal()

"""

"""
Plantear una función que reciba un string en mayúsculas o minúsculas y retorne la cantidad de letras 'a' o 'A'.

def ingresar_datos (valor):

    cantidad = 0

    for x in range (len(valor)):

        if valor[x] == "a" or valor[x] == "A":
            cantidad += 1
    return cantidad

x = input("Ingresa la palabra: ")
ca = ingresar_datos(x)

print("Cantidad de letras en A o a es: ", ca, " La palabra es: ", x)

"""


