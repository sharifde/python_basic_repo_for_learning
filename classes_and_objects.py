# classes_and_objects.py
# This script demonstrates basic Object-Oriented Programming (OOP) in Python

# --------- 1. Defining a Class ---------
# Use case: Represent a simple person

class Person:
    # Constructor (initializer method)
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age

    # Method to display info
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


# --------- 2. Creating Objects ---------

person1 = Person("Sharif", 25)
person2 = Person("Sara", 30)

# Call methods on the objects
person1.introduce()
person2.introduce()


# --------- 3. Class with Default Values ---------

class Dog:
    def __init__(self, name, breed="Unknown"):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof!")

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max")  # uses default breed

dog1.bark()
dog2.bark()
print("Dog2 breed:", dog2.breed)


# --------- 4. Inheritance ---------
# Use case: Create a child class that inherits from a parent class

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name} makes a sound.")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} says: Meow!")

class Cow(Animal):
    def make_sound(self):
        print(f"{self.name} says: Moo!")

cat = Cat("Whiskers")
cow = Cow("Daisy")

cat.make_sound()
cow.make_sound()


# --------- 5. Encapsulation ---------
# Use case: Hide internal data (simulate with private variables)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount
        print(f"{amount} deposited. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"{amount} withdrawn. Remaining balance: {self.__balance}")

    def get_balance(self):
        return self.__balance

account = BankAccount("Sharif", 1000)
account.deposit(500)
account.withdraw(300)
print("Current balance:", account.get_balance())
# print(account.__balance)  # This will raise an AttributeError


# --------- 6. Class vs Instance Variables ---------

class Counter:
    count = 0  # class variable (shared)

    def __init__(self):
        Counter.count += 1  # access via class name
        self.id = Counter.count  # instance variable (unique)

c1 = Counter()
c2 = Counter()
c3 = Counter()

print(f"Total objects created: {Counter.count}")
print(f"c1 id: {c1.id}, c2 id: {c2.id}, c3 id: {c3.id}")
