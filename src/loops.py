# ============================================================
# MÓDULO 5: Loops
# ============================================================


def contar_hasta(n: int) -> list:
    """
    Retorna una lista con los números del 1 al n (inclusive).
    """
    numeros = []
    for i in range(1, n + 1):
        numeros.append(i)
    return numeros


def tabla_multiplicar(n: int) -> list:
    """
    Retorna una lista con los primeros 10 múltiplos de n.
    Ejemplo: tabla_multiplicar(3) -> [3, 6, 9, ..., 30]
    """
    multiplos = []
    for i in range(1, 11):
        multiplos.append(n * i)
    return multiplos


def suma_digitos(n: int) -> int:
    """
    Retorna la suma de los dígitos de un número entero positivo.
    Ejemplo: suma_digitos(123) -> 6
    """
    suma = 0
    for digito in str(n):
        suma += int(digito)
    return suma


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


def fibonacci(n: int) -> list:
    """
    Retorna los primeros n números de la serie de Fibonacci.
    Ejemplo: fibonacci(6) -> [0, 1, 1, 2, 3, 5]
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib
