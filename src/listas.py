# ============================================================
# MÓDULO 3: Listas
# ============================================================


def suma_lista(numeros: list) -> int | float:
    """
    Retorna la suma de todos los elementos de la lista.
    """
    suma = 0
    for numero in numeros:
        suma += numero
    return suma


def filtrar_pares(numeros: list) -> list:
    """
    Retorna una nueva lista con solo los números pares.
    """
    nueva_lista = []
    for numero in numeros:
        if numero % 2 == 0:
            nueva_lista.append(numero)
    return nueva_lista


def invertir_lista(lista: list) -> list:
    """
    Retorna la lista invertida SIN modificar la original.
    """
    nueva_lista = []
    for i in range(len(lista)-1, -1, -1):
        nueva_lista.append(lista[i])
    return nueva_lista
    

def eliminar_duplicados(lista: list) -> list:
    """
    Retorna una nueva lista sin elementos duplicados,
    manteniendo el orden de primera aparición.
    """
    nueva_lista = []
    for elemento in lista:
        if elemento not in nueva_lista:
            nueva_lista.append(elemento)
        return nueva_lista


def aplanar_lista(lista: list) -> list:
    """
    Dada una lista de listas, retorna todos los elementos en una sola lista.
    Ejemplo: aplanar_lista([[1,2],[3,4]]) -> [1, 2, 3, 4]
    """
    nueva_lista = []
    for listaInterior in lista:
        for dato in listaInterior:
            nueva_lista.append(dato)
    return nueva_lista
