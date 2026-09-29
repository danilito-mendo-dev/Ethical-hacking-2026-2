usuarios = [
    {"name": "Jorva", "role": "Admin"},
    {"name": "Iosu", "role": "Developer"},
    {"name": "Ana", "role": "Admin"},
    {"name": "Garcia", "role": "Tester"}
]

roles_unicos = []
for u in usuarios:
    if u["role"] not in roles_unicos:
        roles_unicos.append(u["role"])

print(roles_unicos)