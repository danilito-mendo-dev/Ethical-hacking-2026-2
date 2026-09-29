#Escribe una función que siga pidiendo 
# la edad hasta que se ingrese un número entero válido entre 0 y 120.

def pedir_edad():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            if 0 <= edad <= 120:
                return edad
            else:
                print("La edad debe estar entre 0 y 120")
        except ValueError:
            print("Por favor ingresa un número entero válido")

edad = pedir_edad()
print("Edad valida:", edad)