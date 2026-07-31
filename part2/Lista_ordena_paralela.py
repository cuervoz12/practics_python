"""
Confeccionar un programa que permita cargar los nombres de 5 alumnos y sus notas respectivas. Luego ordenar las notas de mayor a menor. Imprimir las notas y los nombres de los alumnos.

alumnos = []
notas = []

for x in range (5):
    
    a = input("Ingresa el nombre de los alumnos: ")
    alumnos.append(a)
    b = int(input("Ingresa la nota de los alumnos: "))
    notas.append(b)

print("Alumnos y notas desordenadas")
print(alumnos)
print(notas)

for x in range (5):
    
    for y in range (4):
        
        if notas[y] < notas[y+1]:
            auxa = notas[y]
            notas[y] = notas[y+1]
            notas[y+1] = auxa
            auxn = alumnos[y]
            alumnos[y] = alumnos[y+1]
            alumnos[y+1] = auxn
            
print("Alumnos nota mayor a menor")

for x in range (5):
    
    print(alumnos[x], " : " ,notas[x])
    
"""

"""
Crear y cargar en un lista los nombres de 5 países y en otra lista paralela la cantidad de habitantes del mismo. Ordenar alfabéticamente e imprimir los resultados. Por último ordenar con respecto a la cantidad de habitantes (de mayor a menor) e imprimir nuevamente.

paises = []
habitantes = []

for x in range (5):
    
    a = input("Ingresa el nombre del pais: ")
    paises.append(a)
    b = int(input("Ingresa los habitantes: "))
    habitantes.append(b)

for x in range (5):
    
    for y in range (4):
        
        if paises[y] > paises[y+1]:
            aux = paises[y]
            paises[y] = paises[y+1]
            paises[y+1] = aux
            auxh = habitantes[y]
            habitantes[y] = habitantes[y+1]
            habitantes[y+1] = auxh

print("Paises ordenados alfabeticamente ")
for x in range (5):
    
    print(paises[x], habitantes[x])

for x in range (5):
    
    for y in range (4):
        
        if habitantes[y] < habitantes[y+1]:
            aux = paises[y]
            paises[y] = paises[y+1]
            paises[y+1] = aux
            auxh = habitantes[y]
            habitantes[y] = habitantes[y+1]
            habitantes[y+1] = auxh

print("Paises ordenados de mayor a menor ")
for x in range (5):
    
    print(paises[x], habitantes[x])

"""

