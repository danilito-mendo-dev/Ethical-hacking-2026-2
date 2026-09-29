estudiantes = list()

estudiantes.append({"name": "Jordan", "grade": 8})
estudiantes.append({"name": "Ana", "grade": 5})
estudiantes.append({"name": "Jandry", "grade": 9})
estudiantes.append({"name": "iosu", "grade": 6})

aprobados = list()

for e in estudiantes:
    if e["grade"] >= 7:
        aprobados.append(e["name"])

print(f"Estudiantes que pasaron: {aprobados}")