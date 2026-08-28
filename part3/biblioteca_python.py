""""
Confeccionar un programa que simule tirar dos dados y luego muestre los valores que salieron. Imprimir un mensaje que ganó si la suma de los mismos es igual a 7.

import random 

dado1 = random.randint(1,6)
dado2 = random.randint(1, 6)
print("Primer dado: ", dado1)
print("Segundo dado: ", dado2)
suma = dado1 + dado2

if suma == 7:
    print("Ganaste")
else:
    print("Perdiste")
    
"""

"""
Desarrollar un programa que cargue una lista con 10 enteros.
Cargar los valores aleatorios con números enteros comprendidos entre 0 y 1000.
Mostrar la lista por pantalla.
Luego mezclar los elementos de la lista y volver a mostrarlo.

import random

def cargar_datos():

    lista = []

    for x in range (10):

        lista.append(random.randint(0,1000))
    return lista

def mostrar_lista (lista):

    print(lista)

def mezclar_lista (lista):

    random.shuffle(lista)

lista = cargar_datos ()
mostrar_lista (lista)
mezclar_lista (lista)
mostrar_lista (lista)

"""

"""
Confeccionar un programa que genere un número aleatorio entre 1 y 100 y no se muestre.
El operador debe tratar de adivinar el número ingresado.
Cada vez que ingrese un número mostrar un mensaje "Gano" si es igual al generado o "El número aleatorio es mayor" o "El número aleatorio es menor".
Mostrar cuando gana el jugador cuantos intentos necesitó.

import random

x = 0
intentos = 0
numero_oculto = random.randint(1, 100)
print ("Hola ingresa un numero para poder ganar \n")

while x == 0:

    y = int((input("Ingresa el numero: ")))
    intentos += 1
    if y > numero_oculto:
        print("El número aleatorio es menor\n")
    elif y < numero_oculto:
        print("El número aleatorio es mayor\n")
    else:
        print("Gano\n")
        print("Necesitaste", intentos, "intentos")
        x += 1

"""

"""
Confeccionar una programa con las siguientes funciones:
1) Generar una lista con 4 elementos enteros aleatorios comprendidos entre 1 y 3. Agregar un quinto elemento con un 1.
2) Controlar que el primer elemento de la lista sea un 1, en el caso que haya un 2 o 3 mezclar la lista y volver a controlar hasta que haya un 1.
3) Imprimir la lista.

import random

def cargar_datos ():

    lista = []

    for x in range (4):

        lista.append(random.randint(1, 3))
    lista.append (1)
    return lista

def mezclar (lista):

    while lista[0] != 1:

        random.shuffle (lista)

def imprimir_lista (lista):

    print(lista)

lista = cargar_datos ()
imprimir_lista (lista)
mezclar (lista)
imprimir_lista (lista)

"""

