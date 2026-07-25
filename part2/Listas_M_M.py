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

