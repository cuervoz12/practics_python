"""
rear y cargar una lista con los nombres de tres alumnos. Cada alumno tiene dos notas, almacenar las notas en una lista paralela. Cada componente de la lista paralela debe ser también una lista con las dos notas. Imprimir luego cada nombre y sus dos notas.
  
nombres = []
notas = []

for x in range (3):
    
    a = input("Ingresa un nombre: ")
    nombres.append(a)
    no1 = int(input("Ingresa una nota: "))
    no2 = int(input("Ingresa una nota: "))
    notas.append([no1, no2])

for x in range (3):
    
    print("Alumno: ", nombres[x], "sus notas: ", "[ ", notas[x][0], " ] , [ " ,notas[x][1], " ]")  
    
"""

    