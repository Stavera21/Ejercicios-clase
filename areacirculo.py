import math

def calcular_area_circulo(radio):
    area = math.pi * radio**2
    return area
radio = int(input("Ingrese el radio del circulo: "))
area_del_circulo = calcular_area_circulo(radio)
print(f"El area del circulo {area_del_circulo}")