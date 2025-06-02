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
    
