users = list()

users.append({"id": 1, "name": "Jordan", "email": "jordan@gmail.com", "rol": "Admin", "edad": 22})
users.append({"id": 2, "name": "Ana", "email": "ana@gmail.com", "rol": "Usuario", "edad": 22})
users.append({"id": 3, "name": "Jandry", "email": "jandry@gmail.com", "rol": "Usuario", "edad": 22})
users.append({"id": 4, "name": "iosu", "email": "iosu@gmail.com", "rol": "Usuario", "edad": 25})

emails = list()

for u in users:
    emails.append(u["email"])

print(f"Emails: {emails}")