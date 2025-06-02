class Car:
    pass

class Bmw(Car):
    pass

class X6(Bmw):
    pass

print(issubclass(X6, (Car, int))) 
# Output: True

# class definitions
class Animal:
    def speak(self):
        return "Animal speaks"
class Dog(Animal):
    def speak(self):
        return "Dog barks"
class Cat(Animal):
    def speak(self):
        return "Cat meows"
# polymorphism example
def animal_sound(animal):
    return animal.speak()

# example usage
dog = Dog()
cat = Cat() 

print(animal_sound(dog))  # Output: Dog barks
print(animal_sound(cat))  # Output: Cat meows
# example of inheritance
class Vehicle:
    def start(self):
        return "Vehicle started"
# subclassing
class Car(Vehicle):
    def start(self):
        return "Car started"
class Bike(Vehicle):
    def start(self):
        return "Bike started"
# example usage
car = Car()
bike = Bike()
print(car.start())  # Output: Car started
print(bike.start())  # Output: Bike started
# example of encapsulation
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited: {amount}, New Balance: {self.__balance}"
        return "Deposit amount must be positive"

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew: {amount}, New Balance: {self.__balance}"
        return "Insufficient funds or invalid withdrawal amount"

    def get_balance(self):
        return self.__balance  # public method to access private attribute

# example usage
account = BankAccount(100)
print(account.deposit(50))  # Deposited: 50, New Balance: 150
print(account.withdraw(30))  # Withdrew: 30, New Balance: 120
print(account.get_balance())  # 120
# example of abstraction
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
    def perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")
    def description(self):
        return "This is a shape"
class Circle(Shape):
    def __init__(self):
        super().__init__()
