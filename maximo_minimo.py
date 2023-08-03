def encontrar_maximo_minimo(numeros):
    maximo = max(numeros)
    minimo = min(numeros)
    return maximo, minimo

# Ejemplo de uso:
lista_numeros = [45, 67, 12, 98, 23, 56]
maximo, minimo = encontrar_maximo_minimo(lista_numeros)
print("El número más grande es:", maximo)
print("El número más pequeño es:", minimo)
