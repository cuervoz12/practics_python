""""
lista1=[0,1,2,3,4,5,6]
print(lista1[-1]) 
print(lista1[-2]) 

"""

"""
Confeccionar una función que reciba una palabra y verifique si es capicúa (es decir que se lee igual de izquierda a derecha que de derecha a izquierda)

def capicua (cadena):

    indice = -1
    iguales = 0

    for x in range (0, len(cadena) // 2):

        if cadena[x] == cadena[indice]:
            iguales += 1
        indice -= 1
    print(cadena)
    if cadena[x] == cadena[indice]:
        print("Es capicua")
    else:
        print("No es capicua")

capicua("neuquen")
capicua("casa")

"""

"""
Cargar una cadena de caracteres por teclado. Mostrar la cadena del final al principio utilizando subíndices negativos.

palabra=input("Ingresar una palabra:")
indice=-1

for x in range(len(palabra)):

    print(palabra[indice],end="")
    indice=indice-1

"""

"""
Confeccionar un programa con las siguientes funciones:
1) Cargar una lista con 5 palabras.
2) Intercambiar la primer palabra con la última.
3) Imprimir la lista

def cargar():

    palabras=[]

    for x in range(0,5):
    
        pal=input("Ingrese una palabra:")
        palabras.append(pal)
    return palabras

def intercambiar(palabras):

    aux=palabras[0]
    palabras[0]=palabras[-1]
    palabras[-1]=aux

def imprimir(palabras):

    print(palabras)

palabras=cargar()
imprimir(palabras)
intercambiar(palabras)
imprimir(palabras)
"""


