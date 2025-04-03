
from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract Base Class
    @abstractmethod
    def make_sound(self):
        pass  # Must be implemented in subclasses

# Concrete class (subclass) implementing the abstract method
class Dog(Animal):
    def make_sound(self):
        print("Bark!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# dog = Animal()  # ❌ ERROR! Cannot instantiate an abstract class
dog = Dog()
dog.make_sound()  # ✅ Output: Bark!

cat = Cat()
cat.make_sound()  # ✅ Output: Meow!









from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        print("Starting engine...")  # Default implementation

class Car(Vehicle):
    def start_engine(self):  # Overriding
        print("Car engine started!")

class Bike(Vehicle):
    pass  # Uses the default implementation

car = Car()
car.start_engine()  # Output: Car engine started!

bike = Bike()
bike.start_engine()  # Output: Starting engine...