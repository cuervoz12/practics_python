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


```