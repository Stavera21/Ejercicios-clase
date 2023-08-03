def calcular_media_aritmetica(lista):
    return sum(lista) / len(lista)

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
media = calcular_media_aritmetica(lista_numeros)
print(f"La media aritmética de la lista es: {media}")
