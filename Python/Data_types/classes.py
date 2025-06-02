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
    def area(self):
        return "Area of Circle"
    def perimeter(self):
        return "Perimeter of Circle"
class Square(Shape):
    def __init__(self):
        super().__init__()
    def area(self):
        return "Area of Square"
    def perimeter(self):
        return "Perimeter of Square"
class Rectangle(Shape):
    def __init__(self):
        super().__init__()
    def area(self):
        return "Area of Rectangle"
    def perimeter(self):
        return "Perimeter of Rectangle"
# example usage
shapes = [Circle(), Square(), Rectangle()]
for shape in shapes:
    print(shape.description())
    print(shape.area())
    print(shape.perimeter())
    print()  # for better readability
# example of multiple inheritance
class A:
    def method_a(self):
        return "Method A from class A"
class B:
    def method_b(self):
        return "Method B from class B"
class C(A, B):
    def method_c(self):
        return "Method C from class C"
# example usage
c_instance = C()
print(c_instance.method_a())  # Output: Method A from class A
print(c_instance.method_b())  # Output: Method B from class B
print(c_instance.method_c())  # Output: Method C from class C

# method overriding example
class Parent:
    def greet(self):
        return "Hello from Parent"
class Child(Parent):
    def greet(self):
        return "Hello from Child"
# example usage
parent_instance = Parent()
child_instance = Child()
print(parent_instance.greet())  # Output: Hello from Parent
print(child_instance.greet())  # Output: Hello from Child

# example of class method   
class MyClass:
    class_variable = "I am a class variable"

    @classmethod
    def class_method(cls):
        return cls.class_variable
    
# example usage
my_instance = MyClass()
print(my_instance.class_method())  # Output: I am a class variable