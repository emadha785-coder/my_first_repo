class Person():
    def __init__(self,name,age):
        self.name = name
        self.age  = age

    def showInfo(self):
        return f"Your name is {self.name} and your age is {self.age}"
    def age_in_days(self):
        return self.age * 365

name = input("Enter your name: ")
age = int(input("Enter your age: "))

p1 = Person(name, age)

print(p1.showInfo())
print(f"Your age in days is {p1.age_in_days()}")
