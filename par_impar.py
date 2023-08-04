def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"
numero_usuario = int(input("Ingrese un número: "))

resultado = es_par_o_impar(numero_usuario)

print(f"El número {numero_usuario} es {resultado}.")
