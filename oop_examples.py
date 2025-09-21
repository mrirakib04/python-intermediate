# oop_examples.py


# 1. Classes & Objects
class Person:
    def __init__(self, name, age):
        self.name = name  # attribute
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}, I am {self.age} years old.")


p1 = Person("Rakib", 18)
p1.introduce()


# 2. Inheritance & Polymorphism
class Animal:
    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


animals = [Dog(), Cat(), Animal()]
for a in animals:
    print(a.speak())  # Polymorphism in action


# 3. Encapsulation & Abstraction
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private attribute (encapsulation)

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


account = BankAccount("Rakib", 1000)
account.deposit(500)
account.withdraw(200)
print("Balance:", account.get_balance())


# 4. Magic (Dunder) Methods
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title}, Pages: {self.pages}"

    def __len__(self):
        return self.pages

    def __add__(self, other):
        return self.pages + other.pages


b1 = Book("Python Basics", 300)
b2 = Book("Advanced Python", 400)

print(b1)  # __str__
print("Length:", len(b1))  # __len__
print("Total pages:", b1 + b2)  # __add__
