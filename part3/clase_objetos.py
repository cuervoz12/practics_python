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


