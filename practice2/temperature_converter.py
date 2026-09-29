#Escribe una función celsius_to_fahrenheit(c) y su inversa. 
# Maneja entradas no numéricas con try/except.

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

try:
    valor = float(input("Ingrese la temperatura en Celsius: "))
    print(f"{valor}°C = {celsius_to_fahrenheit(valor)}°F")
except ValueError:
    print("Ingresar un número valido")