"""
Confeccionar una función que reciba el nombre de un operario, el pago por hora y la cantidad de horas trabajadas. Debe mostrar su sueldo y el nombre. Hacer la llamada de la función mediante argumentos nombrados.

def calcular_sueld (nombre, costohora, cantidadhoras):

    sueldo = costohora * cantidadhoras
    print(nombre, " Trabajo ", cantidadhoras ," y cobro un sueldo de ", sueldo)

calcular_sueld ("Juan", 10, 120)
calcular_sueld (costohora= 12, cantidadhoras= 40, nombre = "Ana")
calcular_sueld (cantidadhoras= 90, nombre= "Luis", costohora= 7)

"""

"""
Cargar una lista de 10 enteros, luego mostrarlos por pantalla a cada elemento separados por una coma.

"""

def cargar ():

    lista = []

    for x in range (10):

        y = int(input("Ingresar un datos: "))
        lista.append(y)

    for x in range (len(lista)):

        print(lista[x], end= ",")

cargar ()
