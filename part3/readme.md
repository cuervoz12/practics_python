## NOTAS 

```
Vamos a ver otra estructura de datos llamada Tupla.
Una tupla permite almacenar una colección de datos no necesariamente del mismo tipo. Los datos de la tupla son inmutables a diferencia de las listas que son mutables.
Una vez inicializada la tupla no podemos agregar, borrar o modificar sus elementos. 
Utilizamos una tupla para agrupar datos que por su naturaleza están relacionados y que no serán modificados durante la ejecución del programa.

- tuple():  sirve para convertir algo en una tupla.
lista = [1, 2, 3]
tupla = tuple(lista)
print(tupla)

- return sirve para devolver un valor desde una función. Si después de return ponemos varios valores separados por comas, Python los devuelve como una tupla. Si usamos corchetes [], estamos devolviendo una lista.

- Existen dos forma de recorrer listas o tuplas de la forma tradicional la que siempre hemos hecho la cual se utiliza cuando vamos a modificar elementos y la segunda forma que se usa sin indicar subindices 

-Un diccionario está formado por claves (key) y valores (value), y esos valores pueden ser de cualquier tipo, incluso listas, tuplas u otros diccionarios.  Un diccionario puede contener listas, tuplas y otros diccionarios como valores. Esto permite representar información más compleja y organizar datos relacionados dentro de una misma estructura.

- Una porción de una lista, tupla o cadena de caracteres en Python es una parte de esa secuencia que se puede obtener utilizando índices. Se realiza mediante la sintaxis [inicio:fin:paso], donde el inicio indica desde dónde comenzar, el fin indica hasta dónde tomar los elementos sin incluir esa posición y el paso indica cuánto avanzar.
Para recuperar una "porción" o trozo de una lista debemos indicar en el subíndice dos valores separados por el caracter ":".
Del lado izquierdo indicamos a partir de que elementos queremos recuperar y del lado derecho hasta cual posición sin incluir dicho valor.

- podemos utilizar un valor negativo para acceder a un elemento de la estructura de datos como tuplas o listas.
En Python podemos acceder fácilmente al último elemento de la secuencia indicando un subíndice -1 y asi con los otros.

- La biblioteca random de Python permite generar valores y realizar selecciones de forma aleatoria. Es útil para juegos, simulaciones, ejercicios y programas donde se necesite obtener resultados al azar.
+ randint() permite generar un número entero aleatorio dentro de un rango determinado, incluyendo tanto el valor inicial como el final. Por ejemplo, random.randint(1, 10) puede generar cualquier número entre 1 y 10.
+ shuffle() sirve para mezclar aleatoriamente los elementos de una lista, cambiando su orden. Por ejemplo, random.shuffle(lista) reorganiza los elementos de lista de manera aleatoria.

- math: de Python contiene funciones y herramientas para realizar operaciones matemáticas de manera sencilla. Permite trabajar con raíces, potencias, números aleatorios, funciones trigonométricas, redondeos y constantes matemáticas.
+ sqrt(): calcula la raíz cuadrada de un número.
+ pow(): calcula una potencia. Recibe el número base y el exponente.
+ factorial(): es una función de la biblioteca math que calcula el factorial de un número.

- Definición de alias para una funcionalidad: Podemos definir un nombre distinto para una funcionalidad que importamos de otro módulo. Esto puede tener como objetivo que nuestro programa sea más legible o evitar que un nombre de función que importamos colisione con un nombre de función de nuestro propio módulo.
+ Como vemos para definir un alias a una funcionalidad que importamos de un módulo debemos disponer la palabra clave as seguida del nuevo nombre: (from math import sqrt as raiz, pow as elevar)
+ Luego para utilizar la funcionalidad que importamos debemos hacerlo mediante el alias y no con el nombre definido en el módulo que importamos: (r1=raiz(valor), r2=elevar(valor,3))


- Conceptos de programación orientada a objetos: 

Conceptos básicos de Objetos:
Un objeto es una entidad independiente con sus propios datos y programación. Las ventanas, menúes, carpetas de archivos pueden ser identificados como objetos; el motor de un auto también es considerado un objeto, en este caso, sus datos (atributos) describen sus características físicas y su programación (métodos) describen el funcionamiento interno y su interrelación con otras partes del automóvil (también objetos).

El concepto renovador de la tecnología de Orientación a Objetos es la suma de funciones a elementos de datos, a esta unión se le llama encapsulamiento.
Por ejemplo, un objeto Auto contiene ruedas, motor, velocidad, color, etc, llamados atributos. Encapsulados con estos datos se encuentran los métodos para arrancar, detenerse, dobla, frenar etc.
La responsabilidad de un objeto auto consiste en realizar las acciones apropiadas y mantener actualizados sus datos internos.
Cuando otra parte del programa (otros objetos) necesitan que el auto realice alguna de estas tareas (por ejemplo, arrancar) le envía un mensaje. A estos objetos que envían mensajes no les interesa la manera en que el objeto auto lleva a cabo sus tareas ni las estructuras de datos que maneja, por ello, están ocultos.
Entonces, un objeto contiene información pública, lo que necesitan los otros objetos para interactuar con él e información privada, interna, lo que necesita el objeto para operar y que es irrelevante para los otros objetos de la aplicación.

- El método __init__ es un método especial de una clase en Python. El objetivo fundamental del método __init__ es inicializar los atributos del objeto que creamos.
Básicamente el método __init__ remplaza al método inicializar
Las ventajas de implementar el método __init__ en lugar del método inicializar son:
+ El método __init__ es el primer método que se ejecuta cuando se crea un objeto.
+ El método __init__ se llama automáticamente. Es decir es imposible de olvidarse de llamarlo ya que se llamará automáticamente.
+ Quien utiliza POO en Python (Programación Orientada a Objetos) conoce el objetivo de este método.
Otras características del método __init__ son:
+ Se ejecuta inmediatamente luego de crear un objeto.
+ El método __init__ no puede retornar dato.
+ el método __init__ puede recibir parámetros que se utilizan normalmente para inicializar atributos.
+ El método __init__ es un método opcional, de todos modos es muy común declararlo.


```