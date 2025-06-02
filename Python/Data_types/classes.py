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