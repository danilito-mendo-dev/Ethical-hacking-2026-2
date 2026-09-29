def saludo():
    return print("hello eord")

def saludo2(name):
    return print("Hola", name)


def sumar(a,b):
    if b==0:
        return print("El segundo numero es cero")
    else:
        return print("La dividion de ",a," y ",b, " es " ,a/b)

saludo2("Jordan")

sumar(3,0)

try:
    var1 = int (input("Ingrese un numero: "))
except ValueError:
    print("El numero ingresado es: ",var1)