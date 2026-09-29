class User:
 def __init__ (self, name,email):
    self.name=name
    self.email=email

    print("User Created")
    def show_information(self):
       return f"name{self.name}, email:{self.email}"

user1=User("Ana","ana@gmail.com")
user2=User("Jordan","jordan@gmail.com")
user3=User("iosu","iosu@gmail.com")

tmp=user1.show_information()
print(tmp)

print(user1.display())
print(user2.display())
print(user3.display())


class Admin(User):
  def __init__(self, name, email):
    super().__init__(name, email)
    self.role = 'admin'
  def display(self):
    return f"{self.name}, {self.email}, {self.role}"

user4= Admin("AdminUSer", "adminuser@gmail.com")
user5= Admin("AdminUSer2", "adminuser@gmail.com")
print(user4.display())
print(user5.display())