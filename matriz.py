def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def generar_matriz(filas, columnas):
    matriz = [[5 for _ in range(columnas)] for _ in range(filas)]
    return matriz

# Ejemplo de uso:
filas = 3
columnas = 4

matriz_generada = generar_matriz(filas, columnas)
imprimir_matriz(matriz_generada)
