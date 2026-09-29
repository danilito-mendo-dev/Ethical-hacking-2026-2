
#Variables

#number = 10

#name = "Jordan Mera"

#activat = True

#Condicionales

#if number>5:
 #   print("El numero es mayor a 5")
#else:
#    print("El numero es menor a 5")

#Bucles

#for i in range(5):
#    print("The number is:",i)

#Listas

#estudiantes = ["Jordan","Ana"]

#for name in estudiantes:
#    print("Son :",name)

#Dictionario

#user = {
  #  "name": "Jordan",
   # "rol": "Estudiante"
#}

#for valor in user.items():
#    print("Son: ", valor)

estudiantes = [
    {"nombre": "Ana", "nota": 8.5},
    {"nombre": "Carlos", "nota": 6.0},
    {"nombre": "Elena", "nota": 9.2},
    {"nombre": "David", "nota": 4.5},
    {"nombre": "Sofia", "nota": 7.8},
    {"nombre": "Mateo", "nota": 5.5},
    {"nombre": "Lucía", "nota": 10.0},
    {"nombre": "Juan", "nota": 3.2},
    {"nombre": "Valeria", "nota": 8.0},
    {"nombre": "Gabriel", "nota": 6.7}
]

for alumno in estudiantes:
    if alumno["nota"]>7:
        print("El estudiante ",alumno["nombre"],"PASA")
    else:
        print("El estudiante ",alumno["nombre"]," No PASA")