numero_ingresado = int(input("Ingrese un número entero no negativo: "))

if numero_ingresado < 0:
    print("El factorial no está definido para números negativos.")
else:
    factorial = 1
    for i in range(1, numero_ingresado + 1):
        factorial *= i

    print(f"El factorial de {numero_ingresado} es: {factorial}")
