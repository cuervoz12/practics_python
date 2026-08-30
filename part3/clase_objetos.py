"""
Implementaremos una clase llamada Persona que tendrá como atributo (variable) su nombre y dos métodos (funciones), uno de dichos métodos inicializará el atributo nombre y el siguiente método mostrará en la pantalla el contenido del mismo.
Definir dos objetos de la clase Persona.

"""

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
