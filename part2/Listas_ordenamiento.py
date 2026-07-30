"""
Se debe crear y cargar una lista donde almacenar 5 sueldos. Desplazar el valor mayor de la lista a la última posición.
    
sueldos = []

for x in range (5):
    
    y = int(input("Ingresa el sueldo: "))
    sueldos.append(y)

print("Lista sin ordenar: ")
print(sueldos)

for x in range (4):
    
    if sueldos[x] > sueldos[x+1]:
        aux = sueldos[x]
        sueldos[x] = sueldos[x+1]
        sueldos[x+1] = aux

print("Lista ordenada: ")
print(sueldos)    
    
"""

"""
Se debe crear y cargar una lista donde almacenar 5 sueldos. Ordenar de menor a mayor la lista.

sueldos = []

for x in range (5):
    
    y = int(input("Ingresa el sueldo: "))
    sueldos.append(y)

print ("sueldos desordenados")
print(sueldos) 

for k in range (4):
    
    for x in range (4):
    
        if sueldos[x] > sueldos[x+1]:
            aux = sueldos[x]
            sueldos[x] = sueldos[x+1]
            sueldos[x+1] = aux
        
print("de menor a mayor: ")
print(sueldos)

"""

"""
Crear una lista y almacenar los nombres de 5 países. Ordenar alfabéticamente la lista e imprimirla.

paises = []

for x in range (5):
    
    y = input("Ingresa un pais: ")
    paises.append(y)

print("paises sin ordenar: ")
print(paises)

for x in range (5):
    
    for k in range (4):
        
        if paises[k] > paises[k+1]:
            aux = paises[k]
            paises[k] = paises[k+1]
            paises[k+1] = aux

print("paises ordenados: ")
print(paises)

"""

"""
Solicitar por teclado la cantidad de empleados que tiene la empresa. Crear y cargar una lista con todos los sueldos de dichos empleados. Imprimir la lista de sueldos ordenamos de menor a mayor.

sueldos = []

a = int(input("Ingresa la cantidad de empleados: "))

for x in range (a):
    
    b = int(input("Ingresa el sueldo de los empleados: "))
    sueldos.append(b)

print("Sueldos sin ordenar: ")
print(sueldos)

for x in range (a - 1):
    
    for k in range (a - 1 - x): 
        
        if sueldos[k] > sueldos[k+1]:
            aux = sueldos[k]
            sueldos[k] = sueldos[k+1]
            sueldos[k+1] = aux
            
print("Sueldos ordenados de menor a mayor: ")
print(sueldos)

"""

"""
Cargar una lista con 5 elementos enteros. Ordenarla de menor a mayor y mostrarla por pantalla, luego ordenar de mayor a menor e imprimir nuevamente.

numeros = [100, 2000, 400, 666, 520]

print("lista desordenada ")
print(numeros)
print()

for x in range (5):
    
    for y in range (4):
        
        if numeros[y] > numeros[y+1]:
            aux = numeros[y]
            numeros[y] = numeros[y+1]
            numeros[y+1] = aux

print("ordenador de menor a mayor: ")
print(numeros)
print()

for a in range (5):
    
    for b in range (4):
        
        if numeros[b] < numeros[b+1]:
            aux = numeros[b]
            numeros[b] = numeros[b+1]
            numeros[b+1] = aux

print("ordenados de mayor a menor: ")
print(numeros) 
 
"""

   
    