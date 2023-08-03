def fahrenheit_a_celsius(grados_fahrenheit):
    grados_celsius = (grados_fahrenheit - 32) * 5/9
    return grados_celsius
temperatura_fahrenheit = float(input("Ingrese los grados Farenheit: "))
temperatura_celsius = fahrenheit_a_celsius(temperatura_fahrenheit)
print(f"{temperatura_fahrenheit} grados Fahrenheit son equivalentes a {temperatura_celsius} grados Celsius.")