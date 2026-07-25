"""
Definir una lista que almacene 5 enteros. Sumar todos sus elementos y mostrar dicha suma.

lista = [1,2,3,4,5]
suma = 0
x = 0

while x < len(lista):
    
    suma += lista[x]
    x += 1 
    
print("La suma de todos los elementos es: ", suma)

"""

"""
Definir una lista por asignación que almacene los nombres de los primeros cuatro meses de año. Mostrar el primer y último elemento de la lista solamente. 

meses = ["Enero", "Frebrero", "Marzo", "Abril"]

print(meses[0])
print(meses[3])

"""

"""
Definir una lista por asignación que almacene en la primer componente el nombre de un alumno y en las dos siguientes sus notas. Imprimir luego el nombre y el promedio de las dos notas.

alumno = ["Ana", 5.0, 5.0]
suma = 0
promedio = 0

suma = alumno[1] + alumno[2]
promedio = suma/2

print("El nombre es: ", alumno[0], " Su promedio es: ", promedio)

"""

"""
Definir por asignación una lista con 8 elementos enteros. Contar cuantos de dichos valores almacenan un valor superior a 100.

lista = [100, 2, 3, 4, 101, 5, 120, 6]
sumar = 0
x = 0

while x < len(lista):
    
    if lista[x] > 100:
        sumar += 1
    x += 1
    
print("Los valores superiores a 100 son: ", sumar)

"""

"""
Definir una lista por asignación con 5 enteros. Mostrar por pantalla solo los elementos con valor iguales o superiores a 7.

lista = [7, 1, 8, 9, 2]
x = 0

while x < len(lista):
    
    if lista[x] >= 7:
        print(lista[x])

    x += 1

"""

"""
Definir una lista que almacene por asignación los nombres de 5 personas. Contar cuantos de esos nombres tienen 5 o más caracteres.


"""

"""
Definir una lista que almacene por asignación los nombres de 5 personas. Contar cuantos de esos nombres tienen 5 o más caracteres

nombres = ["Juan", "andres", "valentina", "ana", "pedro"]
contar = 0
x = 0

while x < len(nombres):
    
    if len(nombres[x]) >= 5:
        contar += 1
    x += 1

print("Los nombres con 5 o mas caracteres es: ", contar)

"""


