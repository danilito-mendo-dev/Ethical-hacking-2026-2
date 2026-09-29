class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Depósito de {amount}. Balance actual: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Fondos insuficientes")
        else:
            self.balance -= amount
            print(f"Retiro de {amount}. Balance actual: {self.balance}")

cuenta = BankAccount(100)
cuenta.deposit(50)
cuenta.withdraw(30)
cuenta.withdraw(1000)