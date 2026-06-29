

VOCALES = {"A", "E", "I", "O", "U"}


# 1: Leer una linea del archivo y convertirla en matriz 3x3 ---
def linea_a_matriz(linea):
    """Convierte una linea de 9 caracteres en una matriz 3x3."""
    linea = linea.strip()
    return [[linea[fila * 3 + col] for col in range(3)] for fila in range(3)]


# 2: Mostrar una matriz 3x3 con formato matricial ---
def mostrar_matriz(matriz):
    """Muestra la matriz por pantalla con formato matricial."""
    for fila in matriz:
        print(" ".join(fila))


# 3: Generar una nueva matriz 3x3 con solo las vocales encontradas ---
def matriz_vocales(matriz):
    """Devuelve una nueva matriz 3x3 con las vocales de la original (resto '*')."""
    vocales_encontradas = [c for fila in matriz for c in fila if c.upper() in VOCALES]
    vocales_encontradas += ["*"] * (9 - len(vocales_encontradas))
    return [[vocales_encontradas[fila * 3 + col] for col in range(3)] for fila in range(3)]


# 4: Actualizar el diccionario de estadísticas con las vocales de la matriz ---
def actualizar_estadisticas(matriz_voc, estadisticas):
    """Incrementa el contador de cada vocal encontrada en la matriz de vocales."""
    for fila in matriz_voc:
        for c in fila:
            if c in estadisticas:
                estadisticas[c] += 1


# 5: Procesar una sola linea del archivo (leer, convertir, mostrar, actualizar) ---
def procesar_linea(linea, estadisticas):
    """Procesa una linea: genera matrices, las muestra y actualiza estadisticas."""
    matriz_original = linea_a_matriz(linea)

    print("Matriz original:")
    mostrar_matriz(matriz_original)

    mat_voc = matriz_vocales(matriz_original)
    print("\nMatriz de vocales:")
    mostrar_matriz(mat_voc)
    print()

    actualizar_estadisticas(mat_voc, estadisticas)


# 6: Mostrar el resumen final de estadisticas ---
def mostrar_resumen(estadisticas, total_matrices):
    """Muestra el resumen final: matrices procesadas, total vocales y conteo por vocal."""
    total_vocales = sum(estadisticas.values())
    print(f"Matricees procesadas: {total_matrices}")
    print(f"Total de vocales encontradas: {total_vocales}")
    for vocal, cantidad in estadisticas.items():
        print(f"{vocal}: {cantidad}")


# main: coordina la ejecución del programa ---
def main():
    nombre_archivo = "datos.txt"
    estadisticas = {"A": 0, "E": 0, "I": 0, "O": 0, "U": 0}
    total_matrices = 0

    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            if len(linea.strip()) == 9:
                procesar_linea(linea, estadisticas)
                total_matrices += 1

    mostrar_resumen(estadisticas, total_matrices)


if __name__ == "__main__":
    main()
