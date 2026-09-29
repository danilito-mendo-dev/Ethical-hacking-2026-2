users = list()

users.append({"id": 1, "name": "Jordan", "email": "jordan@gmail.com", "rol": "Admin", "edad": 22})
users.append({"id": 2, "name": "Ana", "email": "ana@gmail.com", "rol": "Usuario", "edad": 22})
users.append({"id": 3, "name": "Jandry", "email": "jandry@gmail.com", "rol": "Usuario", "edad": 22})
users.append({"id": 4, "name": "iosu", "email": "iosu@gmail.com", "rol": "Usuario", "edad": 25})

counter = list()

for i in users:
    if i["rol"] == "Admin":
        print(f"Usuario: {i['name']}, {i['email']}, {i['rol']}")
        counter.append(i)

print(f"Usuarios con rol de Admin: {len(counter)}")

totalUsers = next(u for u in users if u["id"] ==2)

print(f"Usuario con id de 2: {totalUsers}")