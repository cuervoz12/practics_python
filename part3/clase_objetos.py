"""
Implementaremos una clase llamada Persona que tendrá como atributo (variable) su nombre y dos métodos (funciones), uno de dichos métodos inicializará el atributo nombre y el siguiente método mostrará en la pantalla el contenido del mismo.
Definir dos objetos de la clase Persona.


class persona:

    def inicializar (self, nom):

        self.nombre = nom

    def imprimir (self):

        print("Nombre ", self.nombre)

persona1 = persona ()
persona1.inicializar ("Pedro")
persona1.imprimir ()

persona2 = persona ()
persona2.inicializar ("Carla")
persona2.imprimir ()

"""

"""
Implementar una clase llamada Alumno que tenga como atributos su nombre y su nota. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje si está regular (nota mayor o igual a 4)

Definir dos objetos de la clase Alumno.

class Alumno:

    def inicializar (self, nombre, nota):

        self.nombre = nombre
        self.nota = nota

    def imprimir (self):

        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)

    def mostrar_estado (self):

        if self.nota >= 4:
            print("Regular")
        else:
            print("Libre")

alumno1 = Alumno ()
alumno1.inicializar ("Diego", 2)
alumno1.imprimir ()
alumno1.mostrar_estado ()

alumno2 = Alumno ()
alumno2.inicializar ("Ana", 10)
alumno2.imprimir ()
alumno2.mostrar_estado ()

"""

"""
Confeccionar una clase que permita carga el nombre y la edad de una persona. Mostrar los datos cargados. Imprimir un mensaje si es mayor de edad (edad>=18)

class Persona:

    def iniciar (self, nombre, edad):

        self.nombre = nombre
        self.edad = edad

    def mayor (self):

        if self.edad >= 18:
            print(self.nombre, " Es mayor de edad")
        else:
            print(self.nombre, "No es mayor de edad")

persona1 = Persona ()
persona1.iniciar ("Camila", 15)
persona1.mayor ()

persona2 = Persona ()
persona2.iniciar ("Juan", 20)
persona2.mayor ()

"""

"""
Desarrollar un programa que cargue los lados de un triángulo e implemente los siguientes métodos: inicializar los atributos, imprimir el valor del lado mayor y otro método que muestre si es equilátero o no. El nombre de la clase llamarla Triangulo.

class Triangulo:

    def inicializar (self, lado1, lado2, lado3):

        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def mayor (self):

        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print("El lado 1 es mayor")
        elif self.lado2 > self.lado1 and self.lado2 > self.lado3:
            print("El lado 2 es mayor")
        elif self.lado3 > self.lado1 and self.lado3 > self.lado2:
            print("El lado 3 es mayor")
        else:
            print("Los lados son iguales")

    def equilatero (self):

        if self.lado1 == self.lado2 and self.lado1 == self.lado3 and self.lado2 == self.lado3:
            print("El triangulo es equilatero")
        else:
            print("EL triangulo no es equilatero")

triangulo1 = Triangulo ()
triangulo1.inicializar (1, 2, 3)
triangulo1.mayor ()
triangulo1.equilatero ()

triangulo2 = Triangulo ()
triangulo2.inicializar (2, 2, 2)
triangulo2.mayor ()
triangulo2.equilatero ()

"""




