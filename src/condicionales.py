# ============================================================
# MÓDULO 2: Condicionales
# ============================================================


def clasificar_numero(n: int) -> str:
    """
    Retorna "positivo", "negativo" o "cero" según corresponda.
    """
    if n > 0:
        return "positivo"
    if n < 0:
        return "negativo"
    return "cero"
    

def mayor_de_tres(a: int, b: int, c: int) -> int:
    """
    Retorna el mayor de tres números.
    """
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    return c


def clasificar_nota(nota: float) -> str:
    """
    Retorna la categoría de la nota:
    - nota >= 9: "Sobresaliente"
    - nota >= 7: "Bueno"
    - nota >= 6: "Aprobado"
    - nota < 6:  "Desaprobado"
    """
    if nota >= 9:
        return "Sobresaliente"
    if nota >= 7:
        return "Bueno"
    if nota >= 6:
        return "Aprobado"
    return "Desaprobado"


def es_bisiesto(anio: int) -> bool:
    """
    Retorna True si el año es bisiesto.
    Un año es bisiesto si es divisible por 4,
    excepto los divisibles por 100, salvo que también lo sean por 400.
    """
    if anio % 400 == 0:
        return True
    if anio % 100 == 0:
        return False
    if anio % 4 == 0:
        return True
    return False
