"""
Crear y cargar una lista con 5 enteros. Implementar un algoritmo que identifique el mayor valor de la lista.  

lista = []

for x in range (5):
    
    y = int(input("Ingresa un numero: "))
    lista.append(y)
    
mayor = lista[0]

for x in range (1, 5):
    
    if lista[x] > mayor:
        mayor = lista[x]
        
print("Lista: ", lista)
print("Numero mayor: ", mayor)
  
"""

"""
Crear y cargar una lista con 5 enteros por teclado. Implementar un algoritmo que identifique el menor valor de la lista y la posición donde se encuentra.

lista = []

for x in range (5):
    
    y = int(input("Ingresa un valor: "))
    lista.append(y)
    
menor = lista[0]
posicion = lista[0]

for x in range (1, 5):
    
    if lista[x] < menor:
        menor = lista[x]
        posicion = x
    
print("Lista: ", lista)
print("Numero menor: ", menor)
print("Posicion: ", posicion)

"""

"""
ngresar por teclado los nombres de 5 personas y almacenarlos en una lista. Mostrar el nombre de persona menor en orden alfabético

nombres = []

for x in range (5):
    
    y = input("Ingrese los nombres: ")
    nombres.append(y)
    
menor = nombres[0]

for x in range (1, 5):
    
    if nombres[x] < menor:
        menor = nombres[x]

print("Nombres: ", nombres)
print("Nombre menor alfabetico: ", menor)

"""

"""
Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje si se repite dentro de la lista (es decir si dicho valor se encuentra en 2 o más posiciones en la lista)


lista = []

for x in range (5):
    
    y = int(input("Ingresa un valor: "))
    lista.append(y)
    
mayor = lista[0]
cantidad = 0

for x in range (1, 5):
    
    if lista[x] > mayor:
        mayor = lista[x]

for x in range (5):
    
    if lista[x] == mayor:
        cantidad += 1

if cantidad > 1:
    print("Se repite el numero mayor ")

print("Lista: ", lista)
print("Numero mayor: ", mayor)

"""

"""
Leer 10 números y mostrar: La lista completa. El número mayor.

lista = [1, 2, 5, 8, 20, 56, 100, 435, 70, 79]
mayor = lista[0]

for x in range (10):
    
    if lista[x] > mayor:
        mayor = lista [x]

print("Lista ", lista)
print("Mayor: ", mayor)

"""

"""
Leer 10 números y mostrar: La lista completa. El número menor.

lista = [23, 243, 545, 652, 52, 12, 566, 86, 75, 68]
menor = lista[0]

for x in range (10):
    
    if lista[x] < menor:
        menor = lista[x]
        
print(lista)
print("menor: ", menor)

"""

"""
Leer 8 números y mostrar: El mayor. El menor.

lista = [32, 423, 654, 21, 43, 7, 23, 64]
mayor = lista[0]
menor = lista[0]

for x in range (8):
    
    if lista[x] > mayor:
        mayor = lista[x]
        
for x in range (8):
    
    if lista[x] < menor:
        menor = lista[x]

print("lista: ", lista)
print("mayor: ", mayor)  
print("menor: ", menor)  

"""

"""
Leer 10 números y mostrar: El mayor. La posición donde se encuentra.

lista = [123, 243, 543, 53, 132, 32, 43, 54, 13, 56]
mayor = lista[0]
posicion = 0

for x in range (10):
    
    if lista[x] > mayor:
        mayor = lista[x]
        posicion = x
        
print(lista)
print("mayor: ", mayor)
print("posicion: ", posicion)

"""

"""
Leer 10 números y mostrar: El menor. La posición donde se encuentra.

lista = [34, 23, 453, 353, 13, 44, 32, 1, 343, 12]
menor = lista[0]
posicion = 0

for x in range (10):
    
    if lista[x] < menor:
        menor = lista[x]
        posicion = x

print(lista)
print("Menor: ", menor)
print("Posicion: ", posicion)

"""

"""
Si el mayor aparece varias veces, mostrar todas sus posiciones.

lista = [8, 12, 5, 12, 3, 12]
mayor = lista[0]
listac = []

for x in range (6):
    
    if lista [x] > mayor:
        mayor = lista[x]
    
for x in range (6):
    
    if lista[x] == mayor:
        listac.append(x)

print(lista)
print("Mayor: ", mayor)
print("Posiciones: ", listac)

"""

"""
Leer 10 números e informar: Cuántos son positivos. Cuántos son negativos. Cuántos son cero.

lista = []
positivos = 0
negativos = 0
ceros = 0

for x in range (1, 11):
    
    y = int(input("Ingresa un numero: "))
    lista.append(y)
    
    if y == 0:
        ceros += 1
    elif y > 0:
        positivos += 1
    else:
        negativos += 1

print(lista)
print("Positivos: ", positivos)
print("Negativos: ", negativos)
print("Ceros: ", ceros)

"""

"""
Leer 10 números y mostrar: Cantidad de números pares. Cantidad de números impares.

lista = [2, 4, 6, 8, 10, 12, 3, 5, 7, 9]
pares = 0
impares = 0

for x in range (10):
    
    if lista[x] % 2 == 0:
        pares += 1
    else:
        impares +=1
        
print(lista)
print("Pares: ", pares)
print("Impares: ", impares)

"""

"""
Leer 10 números y sumar únicamente los números mayores que 100.

lista = [23, 43, 62, 83, 101, 120, 31, 53, 74, 91]
suma = 0

for x in range (10):
    
    if lista[x] > 100:
        suma += lista[x]
        
print(lista)
print("suma: ", suma)

"""

"""
Leer 10 números y mostrar el segundo número más grande.

lista = [5, 8, 20, 17, 20, 10]
mayor = lista[0]
segundo = lista[0]

for x in range (6):
    
    if lista[x] > mayor:
        mayor = lista[x]
    if lista[x] < mayor and lista[x] > segundo:
        segundo = lista[x]

print(lista)
print("Mayor: ", mayor)
print("Segundo: ", segundo)

"""

"""
Leer 10 números y mostrar el segundo número más pequeño.

lista = [5, 8, 20, 17, 20, 10]
mayor = lista[0]
segundo = lista[1]

for x in range (6):
    
    if lista[x] < mayor:
        mayor = lista[x]
    if lista[x] > mayor and lista[x] < segundo:
        segundo = lista[x]

print(lista)
print("Mayor: ", mayor)
print("Segundo: ", segundo)

"""  

"""  
Leer 10 números y decir si todos son iguales.

lista2 = [5, 8, 20, 17, 20, 10, 1, 1, 1, 1]
lista = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
igual = lista[1]
y = 0

for x in range (10):
    
    if lista[x] != igual:
        y += 1

print(lista)

if y == 0:
    print("Todos son iguales ")
else: 
    print("Todos no son iguales")

"""  

"""  
Leer 10 números y decir si están ordenados de menor a mayor.

lista = [5, 8, 20, 17, 24]
lista2 = [1, 2, 3, 4, 5]
y = 0

for x in range (4):
    
    if lista[x] > lista[x+1]:
        y += 1

print(lista)
if y != 0:
    print("la lista no esta ordenada ")
else:
    print("la lista esta ordenada")

"""      

""" 
Leer 5 nombres y mostrar: El primero alfabéticamente. El último alfabéticamente.

nombre = ["ana", "alejandra", "valentina", "andres", "sara"]
mayor = nombre[0]
menor = nombre[0]

for x in range (5):
    
    if nombre[x] > mayor:
        mayor = nombre[x]
    if nombre[x] < menor:
        menor = nombre[x]
        
print(nombre)
print("primero alfabeticamente: ", menor)
print("menor alfabeticamente: ", mayor)

""" 

        


        