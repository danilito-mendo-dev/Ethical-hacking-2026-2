from utils import is_valid_email

correo = input("Ingresa tu correo: ")
if is_valid_email(correo):
    print("Correo válido")
else:
    print("Correo inválido")