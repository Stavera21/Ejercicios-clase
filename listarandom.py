import random

def generar_lista_numeros_aleatorios(longitud_lista):
    lista_numeros_aleatorios = [random.randint(1, 100) for _ in range(longitud_lista)]
    return lista_numeros_aleatorios

# Generamos una lista de 5 números aleatorios
lista_aleatoria = generar_lista_numeros_aleatorios(5)

# Imprimimos la lista generada
print("Lista de números aleatorios:", lista_aleatoria)
