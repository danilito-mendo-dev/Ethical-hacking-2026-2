users = list()

users.append({"id": 1, "name": "Jordan", "email": "jordan@gmail.com", "rol": "Admin", "edad": 22})
users.append({"id": 2, "name": "Ana", "email": "ana@gmail.com", "rol": "Usuario", "edad": 22})
users.append({"id": 3, "name": "Jandry", "email": "jandry@gmail.com", "rol": "Usuario", "edad": 22})
users.append({"id": 4, "name": "iosu", "email": "iosu@gmail.com", "rol": "Usuario", "edad": 25})

def find_user_by_email(users, email):
    return next((u for u in users if u["email"] == email), None)

resultado = find_user_by_email(users, "jandry@gmail.com")
print(f"Usuario encontrado: {resultado}")

resultado2 = find_user_by_email(users, "no-existe@gmail.com")
print(f"Usuario encontrado: {resultado2}")