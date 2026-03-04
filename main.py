import random
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age  = age
        self.id = random.randint(100000,199999)
    def showInfo(self):
        return f"Your name is {self.name} and your age is {self.age}"
    def age_in_days(self):
        return self.age * 365
    def showID(self):
        print(f"Your ID is: {self.id}")

name = input("Enter your name: ")
age = int(input("Enter your age: "))

p1 = Person(name, age)

print(p1.showInfo())
print(f"Your age in days is {p1.age_in_days()}")
p1.showID()
