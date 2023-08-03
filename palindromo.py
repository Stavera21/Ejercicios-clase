def es_palindromo(cadena):
    cadena = cadena.lower().replace("","")
    return cadena == cadena[::-1]

palabra = str(input("Ingrese una cadena de texto: "))

if es_palindromo(palabra):
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")
