"""
Crear una lista por asignación. La lista tiene que tener cuatro elementos. Cada elemento debe ser una lista de 3 enteros.
Imprimir sus elementos accediendo de diferentes modos.
  
lista=[[1,2,3], [4,5,6], [7,8,9], [10,11,12]]

# imprimir la lista completa 
print(lista)
print("---------")
# Imprimir el primer componente
print(lista[0])
print("---------")
# Imprimir el primer componente de la lista contenida en el primir componente de la lista principal
print(lista[0][0])
print("---------")
# imprimir con un for la lista contenida en el primer componente
for x in range (len(lista[0])):
    
    print(lista[0][x])
print("---------")
# Imprimir cada elemento entero de cada elemento de la lista contenida en la lista
for x in range (len(lista)):
    
    for k in range (len(lista[x])):
        
        print(lista[x][k])
  
"""

"""
Crear una lista por asignación. La lista tiene que tener 2 elementos. Cada elemento debe ser una lista de 5 enteros.
Calcular y mostrar la suma de cada lista contenida en la lista principal.

lista=[[1,1,1,1,1], [2,2,2,2,2]]

suma1 = 0
suma2 = 0

for x in range (len(lista[0])):
    
    suma1 += lista[0][x]

for x in range (len(lista[1])):
    
    suma2 += lista[1][x]
    
print("la primera suma de la lista es: ", suma1)
print("la segunda suma de la lista es: ", suma2)

"""

"""
Crear una lista por asignación. La lista tiene que tener 5 elementos. Cada elemento debe ser una lista, la primera lista tiene que tener un elemento, la segunda dos elementos, la tercera tres elementos y así sucesivamente.
Sumar todos los valores de las listas.

lista = [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]]

suma = 0

for x in range (len(lista)):
    
    for y in range (len(lista[x])):
        
        suma += lista[x][y]

print(lista)
print("La suma de todos los valores es: ", suma)

"""

"""
Se tiene la siguiente lista:
lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]
Imprimir la lista. Luego fijar con el valor cero todos los elementos mayores a 50 del primer elemento de "lista".
Volver a imprimir la lista.

lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]

print("Primer lista")
print(lista)

for x in range (len(lista[0])):
    
    if lista[0][x] > 50:
        lista[0][x] = 0

print("Segunda lista")
print(lista) 

"""

"""
Se tiene la siguiente lista:
lista=[[4,12,5,66], [14,6,25], [3,4,5,67,89,23,1], [78,56]]
Imprimir la lista. Luego fijar con el valor cero todos los elementos mayores a 10 contenidos en todos los elementos de la variable "lista".
Volver a imprimir la lista.

lista=[[4,12,5,66], [14,6,25], [3,4,5,67,89,23,1], [78,56]]

print (lista)

for x in range (len(lista)):
    
    for y in range (len(lista[x])):
        
        if lista[x][y] > 10:
            lista[x][y] = 0

print()
print(lista)

"""

"""
Crear una lista por asignación con la cantidad de elementos de tipo lista que usted desee. Luego imprimir el último elemento de la lista principal.

lista=[[4,12,5,66], [14,6,25], [3,4,5,67,89,23,1], [78,56]]

print(lista[len(lista) - 1])
  
"""

"""
matriz = [[5, 8, 2], [1, 7, 9], [4, 6, 3]]    
Imprime cada fila completa.

matriz = [[5, 8, 2], [1, 7, 9], [4, 6, 3]] 

for x in range (len(matriz)):
    
    print(matriz[x])
    
"""

"""
matriz = [[5, 8, 2], [1, 7, 9], [4, 6, 3]]   
Imprime todos los elementos de la primera fila.
Imprime todos los elementos de la segunda columna.
Cuenta cuántos elementos tiene la matriz.

matriz = [[5, 8, 2], [1, 7, 9], [4, 6, 3]] 
suma = 0

print(matriz)
print()
print(matriz[0])
print()

for x in range (len(matriz)):
    
    print("[",matriz[x][1],"]", end=" ")

print()

for x in range (len(matriz)):
    
    for y in range (len(matriz[x])):
        
        suma +=1

print()
print("Elemento tiene la matriz: ", suma)

"""

"""
matriz = [[5, 8, 2], [1, 7, 9], [4, 6, 3]] 
Encuentra el número mayor de toda la matriz.
Encuentra el número menor.
Calcula la suma de todos los elementos.
Calcula el promedio de todos los elementos.
Cuenta cuántos números son pares.

matriz = [[5, 8, 2], [1, 7, 9], [4, 6, 3]] 
mayor = matriz[0][0]
menor = matriz[0][0]
suma = 0
promedio = 0
pares = 0

for x in range (len(matriz)):
    
    for y in range (len(matriz[x])):
        
        if matriz[x][y] > mayor:
            mayor = matriz[x][y]
        if matriz[x][y] < menor:
            menor = matriz[x][y]
        if matriz[x][y] % 2 == 0:
            pares += 1
        suma += matriz[x][y]
        
promedio = suma/9
       
print("Elemento mayor de la matriz: ", mayor)
print("Elemento menor de la matriz: ", menor)
print("La suma de todos los elementos: ", suma)
print("El promedio de todos los elementos: ", promedio)
print("Elementos que son pares: ", pares)

"""

"""
matriz = [[5, 8, 2], [1, 7, 9], [4, 6, 3]] 
Muestra la suma de cada fila
Encuentra el mayor de cada fila.
Encuentra el menor de cada fila.
Calcula el promedio de cada fila.

matriz = [[5, 8, 2], [1, 7, 9], [4, 6, 3]] 


for x in range (len(matriz)):
    
    suma = 0
    
    for y in range (len(matriz[x])):
        
        suma += matriz[x][y]
    
    print(f"fila {x}: ", suma)

for x in range (len(matriz)):
    
    mayor = matriz[0][0]
    menor = matriz[0][0]
    suma = 0
    promedio = 0
    
    for y in range (len(matriz[x])):
        
        if matriz[x][y] > mayor:
            mayor = matriz[x][y]
        if matriz[x][y] < menor:
            menor = matriz[x][y]
        suma += matriz[x][y]
        promedio = suma/len(matriz)
        
    print(f"Mayor de cada fila {x}: ", mayor)
    print(f"Menor de cada fila {x}: ", menor)
    print(f"Promedio por cada fila {x}: {promedio:.2f}")

"""       
    
"""
matriz = [[5, 8, 2], [1, 7, 9], [4, 6, 3]] 
Suma cada columna.
Encuentra el mayor de cada columna.
Encuentra el menor de cada columna.
Calcula el promedio de cada columna.

matriz = [[5, 8, 2], [1, 7, 9], [4, 6, 3]] 

for x in range (len(matriz)):
    
    suma = 0
    
    for y in range (len(matriz[x])):
        
        suma += matriz[y][x]
        
    print(f"columna {x}: ", suma)

for x in range (len(matriz)):
    
    mayor = matriz[0][x]
    menor = matriz[0][x]
    
    for y in range (len(matriz[x])):
        
        if matriz[y][x] > mayor:
            mayor = matriz[y][x]
        if matriz[y][x] < menor:
            menor = matriz[y][x]

    print(f"mayor de cada columna {x}: ", mayor)
    print(f"menor de cada columna: {x}: ", menor)


for x in range (len(matriz)):
    
    suma = 0
    promedio = 0
    
    for y in range (len(matriz[x])):
        
        suma += matriz[y][x]
        
    promedio = suma / len(matriz)
        
    print(f"columna {x} promedio: ", promedio)

"""

"""
matriz = [[5, 8, 2], [1, 7, 9], [4, 6, 3]] 
Pide un número al usuario y muestra si existe en la matriz.
Si existe, indica en qué fila y columna está.

matriz = [[5, 8, 2], [1, 7, 9], [4, 6, 3]] 
encontado = False

b = int(input("Ingresa un numero: "))
    
for x in range (len(matriz)):
    
    for y in range (len(matriz[x])):
        
        if matriz[x][y] == b:
            encontado = True
            fila = x
            columna = x 

if encontado:
    print("EL numero existe")
    print("fila: ", fila , " columna: ", columna)
else:
    print("No existe")

"""

"""
matriz = [[5, 8, 2], [1, 7, 9], [4, 6, 3]] 
Imprime la diagonal principal.
Calcula la suma de la diagonal principal.
Imprime la diagonal secundaria.
Calcula la suma de la diagonal secundaria.

matriz = [[5, 8, 2], [1, 7, 9], [4, 6, 3]] 
suma = 0
suma2 = 0

for x in range (len(matriz)):
    
    suma += matriz[x][x]
    print("[ ",matriz[x][x]," ]", end = " ")

print("\nla suma diagonal principal es: ", suma)

for x in range (len(matriz)):
    
    suma2 += matriz[x][len(matriz) - 1 - x]
    print("[ ",matriz[x][len(matriz) - 1 - x]," ]", end = " ")

print("\nla suma diagonal secundaria es: ", suma2)

"""

"""
matriz = [[5, 8, 2], [1, 7, 9], [4, 6, 3]] 
Multiplica todos los elementos por 2.
Reemplaza todos los números impares por 0.
Crea una nueva matriz donde cada elemento esté elevado al cuadrado.

matriz = [[5, 8, 2], [1, 7, 9], [4, 6, 3]] 
matrizn = [[5, 8, 2], [1, 7, 9], [4, 6, 3]] 
matrizm = []

for x in range (len(matriz)):
    
    for y in range (len(matriz[x])):
        
        print("[ ",matriz[x][y] * 2," ]", end = " ")

print("\n")

for x in range (len(matriz)):
    
    for y in range (len(matriz[x])):
        
        if matriz[x][y] % 2 != 0:
            matriz[x][y] = 0

print(matriz)
print()

for x in range (len(matrizn)):
    
    matriznueva = []
    
    for y in range (len(matrizn[x])):
        
        matriznueva.append(matrizn[x][y] ** 2)
    
    matrizm.append(matriznueva)

print(matrizm)

"""

"""
matriz = [[5, 8, 2], [1, 7, 9], [4, 6, 3]]
Cuenta cuántos números son mayores que 5.
Encuentra la posición del número mayor.
Determina si la matriz es simétrica.   

matriz = [[5, 8, 2], [1, 7, 9], [4, 6, 3]]
mayor = matriz[0][0]
fila = 0
colmuna = 0
contarcinco = 0
simetrica = True

for x in range (len(matriz)):
    
    for y in range (len(matriz[x])):
        
        if matriz[x][y] > 5:
            contarcinco += 1
        if matriz[x][y] > mayor:
            mayor = matriz[x][y]
            fila = x
            colmuna = y
        if matriz[x][y] != matriz[y][x]:
            simetrica = False

if simetrica:
    print("la matriz es simetrica")
else: 
    print("la matriz no es simetrica")
    
print("Los numeros que son mayores a 5 es: ", contarcinco)
print(f"numero mayor es {mayor} en la fila {fila} en la columna {colmuna}")

"""

"""
Reto final (sin usar max() ni min())

Crea un programa que:

Recorra toda la matriz.
Encuentre el mayor y el menor.
Calcule la suma.
Calcule el promedio.
Cuente cuántos números son pares e impares.
Muestre la posición del mayor y del menor.

matriz = [[5, 8, 2], [1, 7, 9], [4, 6, 3]]
mayor = matriz[0][0]
menor = matriz[0][0]
suma = 0
promedio = 0
pares = 0
impares = 0
posicionfilamayor = 0
posicioncolumnamayor = 0
posicionfilamenor = 0
posicioncolumnamenor = 0

for x in range (len(matriz)):
    
    for y in range (len(matriz[x])):
        
        if matriz[x][y] > mayor:
            mayor = matriz[x][y]
            posicionfilamayor = x
            posicioncolumnamayor = y
        if matriz[x][y] < menor:
            menor = matriz[x][y]
            posicionfilamenor = x
            posicioncolumnamenor = y
        if matriz [x][y] % 2 == 0:
            pares += 1
        if matriz[x][y] % 2 != 0:
            impares += 1
        suma += matriz[x][y]
      
promedio = suma / 9          

print(matriz)
print(f"Numero mayor {mayor} fila {posicionfilamayor} columna {posicioncolumnamayor}")
print(f"Numero menor {menor} fila {posicionfilamenor} columna {posicioncolumnamenor}")
print("La suma de la matriz: ", suma)
print("Promedio de la matriz: ", promedio)
print("numeros pares son: ", pares)
print("numeros impares son: ", impares)
    
"""

