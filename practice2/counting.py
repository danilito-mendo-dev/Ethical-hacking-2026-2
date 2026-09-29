class User:
    contador = 0

    def __init__(self, name):
        self.name = name
        User.contador += 1

    def display(self):
        print(f"Usuario: {self.name}")

u1 = User("Ana")
u2 = User("Jordan")
u3 = User("Iosu")

print("Total de usuarios creados:", User.contador)