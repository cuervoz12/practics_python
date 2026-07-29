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

