"""
Definir una lista vacía y luego solicitar la carga de 5 enteros por teclado y añadirlos a la lista. Imprimir la lista generada.
    
lista = []

for x in range (5):
    
    agregar = int(input("Ingresa 5 numeros a la lista: "))
    lista.append(agregar)
    print(lista)
    
print("Lista completa: ",lista)
        
"""

"""
Realizar la carga de valores enteros por teclado, almacenarlos en una lista. Finalizar la carga de enteros al ingresar el cero. Mostrar finalmente el tamaño de la lista.

lista = []
x = 0

while x == 0:
    
    y = int(input("Ingresa un numero finaliza cuando ingreses 0: "))
    if y == 0:
        print("Proceso finalizado. ")
        x += 1
    else:
        lista.append(y)
      
print("Lista: ", lista)  
print("Tamano de la lista: ", len(lista))

"""

"""
Almacenar en una lista los sueldos (valores float) de 5 operarios. Imprimir la lista y el promedio de sueldos.

sueldos = []
suma = 0
promedio = 0

for x in range (5):
    
    y = float(input("Ingresa el salario: "))
    sueldos.append(y)
    suma += y
    promedio = suma / 5
    
print("Lista: ", sueldos)
print("Promedio de sueldos: ", promedio) 

"""

"""
Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float)
Obtener el promedio de las mismas. Contar cuántas personas son más altas que el promedio y cuántas más bajas.

personas = []
suma = 0
promedio = 0
altas = 0
bajas = 0

for x in range (5):
    
    y = float(input("Ingresa la altura de la persona: "))
    personas.append(y)
    suma += y

promedio = suma / 5

for x in range (5):
    if personas[x] > promedio:
        altas += 1
    else:
        bajas += 1
        
print("Lista: ", personas)
print("Promedio: ", promedio)
print("Mas altas del promedio: ", altas)
print("Mas bajas del promedio: ", bajas)

"""

"""
Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados (4 por la mañana y 4 por la tarde) Confeccionar un programa que permita almacenar los sueldos de los empleados agrupados en dos listas.
Imprimir las dos listas de sueldos.

listam = []
listan = []

for x in range (9):
    
    if x < 4:
        y = float(input("Ingresa el sueldo del turno de la manana: "))
        listam.append(y)
    if x > 4:
        z = float(input("Ingresa el sueldo del turno de la noche: "))
        listan.append(z)

print("")
print("Sueldos de la manana: ", listam)
print("Sueldos de la noche: ", listan)

"""


        
    







