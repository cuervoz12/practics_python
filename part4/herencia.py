"""
Plantear una clase Persona que contenga dos atributos: nombre y edad. Definir como responsabilidades la carga por teclado y su impresión.
En el bloque principal del programa definir un objeto de la clase persona y llamar a sus métodos.

Declarar una segunda clase llamada Empleado que herede de la clase Persona y agregue un atributo sueldo y muestre si debe pagar impuestos (sueldo superior a 3000)
También en el bloque principal del programa crear un objeto de la clase Empleado.

class Persona:

    def __init__ (self):

        self.nombre = input("Ingrese su nombre: ")
        self.edad = int(input("Ingrese su edad: "))


    def imprimir (self):

        print("Nombre: ", self.nombre, " Edad: ", self.edad)

class Empleado (Persona):

    def __init__ (self):

        super().__init__()
        self.sueldo = float(input("Ingresa el sueldo: "))

    def imprimir (self):

        super().imprimir ()
        print("El sueldo: ", self.sueldo)

    def paga_impuestos (self):

        if self.sueldo > 3000:
            print("El empleado debe pagar impuestos")
        else:
            print("No paga impuestos")

persona1 = Persona ()
persona1.imprimir ()
print("____________________________")
empleado1 = Empleado ()
empleado1.imprimir ()
empleado1.paga_impuestos ()

"""

"""

class Operacion:

    def __init__(self):

        self.valor1 = 0
        self.valor2 = 0
        self.resultado = 0

    def cargar1 (self):

        self.valor1 = int(input("Ingrese el valor 1: "))

    def cargar2 (self):

        self.valor2 = int(input("Ingrese el valor 2: "))

    def mostrar_resultado (self):

        print(self.resultado)

    def operar (self):

        pass

class Suma (Operacion):

    def operar (self):

        self.resultado = self.valor1 + self.valor2

class Resta (Operacion):

    def operar (self):

        self.resultado = self.valor1 - self.valor2

suma1 = Suma ()
suma1.cargar1 ()
suma1.cargar2 ()
suma1.operar ()
print("La suma de los dos valores es ")
suma1.mostrar_resultado ()


resta1 = Resta ()
resta1.cargar1 ()
resta1.cargar2 ()
resta1.operar ()
print("La resta de los dos valores es ")
resta1.mostrar_resultado ()

"""

"""
Declarar una clase Cuenta y dos subclases CajaAhorra y PlazoFijo. Definir los atributos y métodos comunes entre una caja de ahorro y un plazo fijo y agruparlos en la clase Cuenta.
Una caja de ahorro y un plazo fijo tienen un nombre de titular y un monto. Un plazo fijo añade un plazo de imposición en días y una tasa de interés. Hacer que la caja de ahorro no genera intereses.
En el bloque principal del programa definir un objeto de la clase CajaAhorro y otro de la clase PlazoFijo.

class Cuenta:

    def __init__(self,titular,monto):
        
        self.titular=titular
        self.monto=monto

    def imprimir(self):

        print("Titular:",self.titular)
        print("Monto:",self.monto)


class CajaAhorro(Cuenta):

    def __init__(self,titular,monto):

        super().__init__(titular,monto)

    def imprimir(self):

        print("Cuenta de caja de ahorro")
        super().imprimir()

class PlazoFijo(Cuenta):

    def __init__(self,titular,monto,plazo,interes):

        super().__init__(titular,monto)
        self.plazo=plazo
        self.interes=interes

    def imprimir(self):

        print("Cuenta de plazo fijo")
        super().imprimir()
        print("Plazo en dias:",self.plazo)
        print("Interes:",self.interes)
        self.ganancia_interes()

    def ganancia_interes(self):

        ganancia=self.monto*self.interes/100
        print("Importe del interes:",ganancia)


cajaahorro=CajaAhorro("Juan", 2000)
cajaahorro.imprimir()

plazofijo=PlazoFijo("Diego", 10000, 30, 0.75)
plazofijo.imprimir()

"""

