class User:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Usuario: {self.name}")

usuarios = [User("Ana"), User("Jordan"), User("Iosu")]

for u in usuarios:
    u.display()