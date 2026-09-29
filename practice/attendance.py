estudiantes = [
    {"name": "Ana", "present": True},
    {"name": "Jandy", "present": False},
    {"name": "Iosu", "present": False}
]

for alumno in estudiantes:
    if not alumno["present"]:
        print(alumno["name"])