# Registro de Prompts

En este archivo debés documentar los prompts que usaste con herramientas de IA
(GitHub Copilot, ChatGPT, etc.) durante el desarrollo del TP.

**¿Por qué?** Queremos que aprendas a trabajar con IA de forma reflexiva:
que sepas qué le pediste, qué obtuviste, y si tuviste que corregirlo.

---

## Formato para cada entrada

```
### [Número] - [Módulo]

**Herramienta**: GitHub Copilot / ChatGPT / otra

**Prompt usado**:
> Escribí acá exactamente lo que le pediste a la IA

**Resultado obtenido**:
Describí brevemente qué generó (código, explicación, etc.)

**¿Lo usaste tal cual o lo modificaste?**
Explicá qué cambios hiciste y por qué (o por qué no cambiaste nada).
```

---

## Mis prompts

### 1 - variables.py

**Herramienta**: 
Chat-gpt
**Prompt usado**:
>Como seria la solucion mas concreta para poder realizar en pocas condiciones la siguiente funcion en python? def es_mayor_de_edad(edad: int) -> bool: """ Retorna True si edad >= 18, False caso contrario. """
def es_mayor_de_edad(edad: int) -> bool:
"""
Retorna True si edad >= 18, False caso contrario.
"""


**Resultado obtenido**:
def es_mayor_de_edad(edad: int) -> bool:
"""
Retorna True si edad >= 18, False caso contrario.
"""
return edad >= 18
Breve idea: la condición ya produce un valor booleano, si se cumple devuelve true, si no devuelve false y no hace falta usar if si solo queres evaluar esa condicion


**¿Lo usaste tal cual o lo modificaste?**

Lo modifique ya que me gustaba mas que quede explicito los returns y que devuelve al ir por cada camino 
---

### 2 - condicionales.py

**Herramienta**: chat gpt

**Prompt usado**:
> Quiero resolver la siguiente funcion en python: def mayor_de_tres(a: int, b: int, c: int) -> int: """ Retorna el mayor de tres números. """, la cual consta como objetivo distinguir el numero mas grande entre las 3 posibles entradas a,b y c. Quiero unicamente el código

**Resultado obtenido**:
def mayor_de_tres(a: int, b: int, c: int) -> int:
if a >= b and a >= c:
return a
if b >= a and b >= c:
return b
return c

**¿Lo usaste tal cual o lo modificaste?**
Si, de hecho lo resolvi y me dio el mismo resultado asi que quedo de la misma forma

---

### 3 - listas.py

**Herramienta**: chat gpt

**Prompt usado**:
> Podrias ayudarme a resolver el siguiente ejercicio de realizar una funcion en python: def aplanar_lista(lista: list) -> list: """ Dada una lista de listas, retorna todos los elementos en una sola lista. Ejemplo: aplanar_lista([[1,2],[3,4]]) -> [1, 2, 3, 4] """ Quiero que te guies en lo que pide o da de ejemplo la descripcion escrita en la función
def aplanar_lista(lista: list) -> list:
"""
Dada una lista de listas, retorna todos los elementos en una sola lista.
Ejemplo: aplanar_lista([[1,2],[3,4]]) -> [1, 2, 3, 4]
"""


**Resultado obtenido**:
resultado = []
for sublista in lista:
for elemento in sublista:
resultado.append(elemento)
return resultado

Qué hace
•	resultado empieza como lista vacía 
•	recorre cada sublista dentro de lista 
•	después recorre cada elemento de esa sublista 
•	lo agrega a resultado 
•	al final devuelve la lista completa


**¿Lo usaste tal cual o lo modificaste?**
Quedo igual pero con variables distintas porque lo estaba encarando de igual manera pero con otro nombre de variable

---

### 4 - diccionarios.py

**Herramienta**: chat gpt

**Prompt usado**:
> necesito una solucion para una funcion invertir_diccionario(d: dict) -> dict: con las siguiente descripcion: """ Retorna un nuevo diccionario con claves y valores intercambiados. Ejemplo: invertir_diccionario({"a": 1}) -> {1: "a"} """ Necesito el codigo de la funcion en python de una forma correcta pero no tan compleja

**Resultado obtenido**:
def invertir_diccionario(d: dict) -> dict:
nuevo = {}
for clave, valor in d.items():
nuevo[valor] = clave
return nuevo


**¿Lo usaste tal cual o lo modificaste?**
Se uso tal cual porque no me acordaba exactamente de como resolverlo

---

### 5 - loops.py

**Herramienta**: chat gpt

**Prompt usado**:
> Ayudame a realizar un loop o logica para poder analizar en python si un numero pasado por parametro es primo, retornando true o false: usa la siguiente funcion de ejemplo: def es_primo(n: int) -> bool: """ Retorna True si n es un número primo. """ # TU CÓDIGO AQUÍ pass

**Resultado obtenido**:
La lógica es si n es menor que 2, no es primo, si n es 2, sí es primo, después hay que probar si tiene divisores exactos, si algún número entre 2 y n - 1 lo divide, no es primo si ninguno lo divide, es primo
def es_primo(n: int) -> bool:
"""
Retorna True si n es un número primo.
"""
if n < 2:
return False
for i in range(2, n):
if n % i == 0:
return False
return True


**¿Lo usaste tal cual o lo modificaste?**
La use tal cual, pero entendiendo como se resolvio y no un copy paste unicamente

---

### 6 - funciones.py

**Herramienta**: chat gpt

**Prompt usado**:
> Tengo una duda sobre esta funcion y lo que pide el ejercicio o descripcion de la def aplicar_funcion : def aplicar_funcion(lista: list, func) -> list: """ Aplica func a cada elemento de la lista y retorna la nueva lista. """ # TU CÓDIGO AQUÍ pass que significa aplicar func y cual seria la solucion a lo que pide la consigna

**Resultado obtenido**:
func significa una función que te pasan como parámetro.
O sea, aplicar_funcion(lista, func) recibe dos cosas:
•	lista: una lista de elementos 
•	func: una función que se va a usar sobre cada elemento de esa lista 
La consigna te está pidiendo algo así:
•	agarrar cada elemento de lista 
•	aplicarle func 
•	guardar el resultado en una nueva lista 
•	devolver esa nueva lista
def aplicar_funcion(lista: list, func) -> list:
"""
Aplica func a cada elemento de la lista y retorna la nueva lista.
"""
nueva_lista = []
for elemento in lista:
nueva_lista.append(func(elemento))
return nueva_lista
Necesito una explicacion y codigo con buenas practicas y correcta (no tan compleja )para darle solucion a esta funcion en python: def componer(f, g): """ Retorna una nueva función que aplica g y luego f. Ejemplo: componer(f, g)(x) == f(g(x)) """
Sí. Esta función no devuelve un número ni una lista: devuelve otra función.
La idea de componer(f, g) es crear una nueva función que, cuando reciba un valor, haga esto en orden:
1.	primero aplica g 
2.	después al resultado le aplica f 
O sea:
componer(f, g)(x) == f(g(x))

def componer(f: Callable, g: Callable) -> Callable:
"""
Retorna una nueva función que aplica g y luego f.
Ejemplo:
componer(f, g)(x) == f(g(x))
"""
def funcion_compuesta(x):
return f(g(x))
return funcion_compuesta
Que significa o que pide concretamente esta funcion? def memoizar(func): """ Retorna una versión de func que cachea sus resultados. Si se llama con los mismos argumentos, retorna el resultado cacheado. """ cache = {} # TU CÓDIGO AQUÍ pass
Pide que hagas una función que reciba otra función y devuelva una versión mejorada que recuerde resultados anteriores.
Eso es memoización.
Qué significa “cachear sus resultados”
Significa esto:
•	la primera vez que llamás a la función con ciertos argumentos, la ejecuta normal 
•	guarda ese resultado en cache 
•	si más adelante la llamás con los mismos argumentos, en vez de recalcular, devuelve lo que ya había guardado
Qué te pide concretamente la consigna
Te pide completar la lógica para que:
1.	se cree una función interna 
2.	esa función reciba argumentos 
3.	revise si esos argumentos ya están en cache 
4.	si están, devuelva el valor guardado 
5.	si no están, ejecute func, guarde el resultado y lo devuelva 
6.	al final, memoizar devuelva esa función nueva
def memoizar(func):
"""
Retorna una versión de func que cachea sus resultados.
Si se llama con los mismos argumentos, retorna el resultado cacheado.
"""
cache = {}
def funcion_memoizada(*args):
if args in cache:
return cache[args]
resultado = func(*args)
cache[args] = resultado
return resultado
return funcion_memoizada
*args
Porque así la función sirve para:
•	una función con un argumento 
•	dos argumentos 
•	tres argumentos 
•	etc.


**¿Lo usaste tal cual o lo modificaste?**
Se uso tal cual porque no sabia como encarar el ejercicio

---

### 7 - operaciones.py

**Herramienta**: chat gpt

**Prompt usado**:
> Segun la siguiente funcion en python como seria la forma adecuada de resolverla haciendo uso de buenas practicas y basandonos si es posible en la teoria adjunta, requiero el codigo y una breve explicacion def contar_vocales(texto: str) -> int: """ Retorna la cantidad de vocales (a,e,i,o,u) en el texto, sin distinguir mayúsculas/minúsculas. """ # TU CÓDIGO AQUÍ pass

**Resultado obtenido**:
Sí. Una forma correcta, simple y alineada con la teoría es:
def contar_vocales(texto: str) -> int:
"""
Retorna la cantidad de vocales (a,e,i,o,u) en el texto,
sin distinguir mayúsculas/minúsculas.
"""
vocales = "aeiou"
cantidad = 0

for caracter in texto.lower():
if caracter in vocales:
cantidad += 1

return cantidad
Explicacion: .lower() convierte todo a minúsculas, for carácter in texto.lower() recorre el texto carácter por carácter sin usar índices, con if carácter in vocales se verifica si el actual es una vocal y se realiza un suma por vocal encontrada


**¿Lo usaste tal cual o lo modificaste?**
No lo modifique, la use tal cual
---

## Reflexión final

Respondé brevemente (3-5 oraciones):

- ¿Qué aprendiste sobre cómo formular buenos prompts?
Es necesario debido que tenemos que saber que es lo que estamos haciendo y no simplemente buscar el atajo mas rapido, pararnos a ver si sabemos analizar aquello que la ia nos responde y usarlo no solo de forma conciente sino para aplicarlo a un ambito mas profesional siempre aprendiendo
- ¿En qué casos la IA fue útil y en cuáles no?
Mas que nada al no saber comandos o cuando un ejercicio es mas complejo a nivel calculo y logica muy rebuscada
- ¿Qué harías diferente la próxima vez?
Aprender mas antes de preguntar, o saber que temas estan involucrados en el problema antes de directamente preguntar a la ia
