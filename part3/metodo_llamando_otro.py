"""
Plantear una clase Operaciones que solicite en el método __init__ la carga de dos enteros e inmediatamente muestre su suma, resta, multiplicación y división. Hacer cada operación en otro método de la clase Operación y llamarlos desde el mismo método __init__

class Operaciones:

    def __init__ (self):

        self.num1 = int(input("Ingrese un valor: "))
        self.num2 = int(input("Ingrese un valor: "))
        self.sumar ()
        self.restar ()
        self.multiplicar ()
        self.division ()

    def sumar (self):

        su = self.num1 + self.num2
        print("La suma es: ", su)

    def restar (self):

        re = self.num1 - self.num2
        print("La resta es: ", re)

    def multiplicar (self):

        mu = self.num1 * self.num2
        print("La multiplicacion es: ", mu)

    def division (self):

        di = self.num1 / self.num2
        print("La division es: ", di)

operacion = Operaciones ()

"""

"""
Plantear una clase que administre dos listas de 5 nombres de alumnos y sus notas. Mostrar un menú de opciones que permita:
1- Cargar alumnos.
2- Listar alumnos.
3- Mostrar alumnos con notas mayores o iguales a 7.
4- Finalizar programa.

class Alumnos:

    def __init__(self):

        self.alumnos = []
        self.notas = []

    def menu(self):

        opcion = 0
        while  opcion != 4:
            print("1- Cargar alumnos")
            print("2- Listar alumnos")
            print("3- Listado de alumnos con notas mayores o iguales a 7")
            print("4- Finalizar programa")
            opcion = int(input("Ingresa la opcion: "))
            if opcion == 1:
                self.cargar()
            elif opcion == 2:
                self.mostrar()
            elif opcion == 3:
                self.mayores()
       
    def cargar (self):

        for x in range (5):
            y = input("Ingresa el nombre del alumno: ")
            z = int(input("Ingresa la nota del alumno: "))
            self.alumnos.append(y)
            self.notas.append(z)
            print("_____________________")   

    def mostrar (self):

        print(self.alumnos)
        print(self.notas)
        print("_____________________")   

    def mayores (self):

        for x in range (5):

            if self.notas[x] >= 7:
                print(self.alumnos[x], self.notas[x])
        print("_____________________")   
     

clase1 = Alumnos()
clase1.menu()

"""

"""
Confeccionar una clase que administre una agenda personal. Se debe almacenar el nombre de la persona, teléfono y mail
Debe mostrar un menú con las siguientes opciones:
1- Carga de un contacto en la agenda.
2- Listado completo de la agenda.
3- Consulta ingresando el nombre de la persona.
4- Modificación de su teléfono y mail.
5- Finalizar programa.

class Agenda:

    def __init__ (self):

        self.contactos = {}

    def menu (self):

        opcion = 0
        while opcion != 4:
            print("1- Carga de un contacto en la agenda")
            print("2- Listado completo de la agenda")
            print("3- Consulta ingresando el nombre de la persona")
            print("4- Modificacion del telefono y mail")
            print("5- Finalizar programa")
            opcion=int(input("Ingrese su opcion:"))
            if opcion == 1:
                self.cargar ()
            elif opcion == 2:
                self.listar ()
            elif opcion == 3:
                self.consultar ()
            elif opcion == 4:
                self.modificar
                
    def cargar (self):

        nombre = input("Ingrese el nombre de la persona: ")
        telefono = int(input("Ingrese el telefono de la persona: "))
        email = input("Ingresa el email de la persona: ")

        self.contactos[nombre] = (telefono, email)
        print("______________________________________________")

    def listar (self):

        print("Listado completo de la agenda")
        for persona in self.contactos:

            print(persona, self.contactos[persona][0], self.contactos[persona][1])
        print("______________________________________________")

    def consultar (self):

        nombres = input("Ingresa el nombre de la persona a consultar: ")
        if nombres == self.contactos:
            print(nombres, self.contactos[nombres][0], self.contactos[nombres][1])
        print("______________________________________________")

    def modificar (self):

        nombre=input("Ingrese el nombre de la persona a modificar el telefono y mail:")
        if nombre in self.contactos:
            telefono = int(input("Ingresa el nuevo telefono: "))
            email = input("Ingresa el nuevo email: ")
            self.contactos[nombre] = (telefono, email)
        else:
            print("No existe un contaxto con ese nombre")
        print("______________________________________________")     

persona1 = Agenda ()
persona1.menu ()

"""


