"""
Confeccionar una clase que represente un empleado. Definir como atributos su nombre y su sueldo. En el método __init__ cargar los atributos por teclado y luego en otro método imprimir sus datos y por último uno que imprima un mensaje si debe pagar impuestos (si el sueldo supera a 3000)

class Empleado ():

    def __init__ (self):

        self.nombre = input("Ingresa el nombre de la persona: ")
        self.sueldo = float(input("Ingrese el sueldo: "))

    def imprimir (self):

        print("El nombre de la persona es: ", self.nombre)
        print("El sueldo de la persona es: ", self.sueldo)

    def paga_impuesto (self):

        if self.sueldo > 3000:
            print("Debe pagar impuestos")
        else:
            print("No paga impuestos")

persona1 = Empleado ()
persona1.imprimir ()
persona1.paga_impuesto ()

"""

"""
Desarrollar una clase que represente un punto en el plano y tenga los siguientes métodos: inicializar los valores de x e y que llegan como parámetros, imprimir en que cuadrante se encuentra dicho punto (concepto matemático, primer cuadrante si x e y son positivas, si x<0 e y>0 segundo cuadrante, etc.)

class Punto:

    def __init__ (self, x, y):

        self.x = x
        self.y = y

    def imprimir (self):

        print("Coordenada del punto")
        print("(",self.x,",",self.y,")")

    def imprimir_cuadrante (self):

        if self.x>0 and self.y>0:
            print("Primer cuadrange")
        else:
            if self.x<0 and self.y>0:
                print("Segundo cuadrante")
            else:
                if self.x<0 and self.y<0:
                    print("Tercer cuadrante")
                else:
                    if self.x>0 and self.y<0:
                        print("Cuarto cuadrante")

punto1= Punto(10,-2)
punto1.imprimir ()
punto1.imprimir_cuadrante ()

"""

"""
Desarrollar una clase que represente un Cuadrado y tenga los siguientes métodos: inicializar el valor del lado llegando como parámetro al método __init__ (definir un atributo llamado lado), imprimir su perímetro y su superficie.

class Cuadrado:

    def __init__ (self, lado):

        self.lado = lado

    def peri_supe (self):

        pero = self.lado * 4
        print("EL perimetro es: ", pero)
        super = self.lado * self.lado
        print("La superficie es: ", super)

cuadrado1 = Cuadrado (5)
cuadrado1.peri_supe ()

"""

"""
Implementar la clase Operaciones. Se deben cargar dos valores enteros por teclado en el método __init__, calcular su suma, resta, multiplicación y división, cada una en un método, imprimir dichos resultados.

class Operaciones:

    def __init__ (self):

        self.num1 = int(input("Ingrese un valor: "))
        self.num2 = int(input("Ingrese un valor: "))

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

operacion1 = Operaciones ()
operacion1.sumar ()
operacion1.restar ()
operacion1.multiplicar ()
operacion1.division ()

"""


