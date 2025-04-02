
#OOP METHODS
#1)Inheritance
#This is where a class inherints properties of another class
   
class Animal:  # Parent class
        def speak(self):
            print("Animal makes a sound")

class Dog(Animal):  # Child class (inherits from Animal)
        def speak(self):
            print("Dog barks")

dog = Dog()
dog.speak()  # Output: Dog barks

#The Dog class inherits from Animal but overrides the speak() method.

#2. Polymorphism (Many Forms)

    #Definition: Polymorphism allows objects of different classes to be treated as objects of a common super class.

   # Analogy: A person can act as a teacher, a driver, or a friend, depending on the situation.

   # Example:

# class Cat:
#         def speak(self):
#             print("Meow")

# class Dog:
#         def speak(self):
#             print("Bark")

#     # Polymorphism in action
# for animal in [Cat(), Dog()]:
#         animal.speak()

#Even though Cat and Dog have different implementations of speak(), we can use the same method name to call them.

#3. Abstraction (Hiding Complexity)

   # Definition: Abstraction hides complex details and only shows the essential features of an object.

  #  Analogy: When you drive a car, you don’t need to know how the engine works—you just use the steering wheel and pedals.

   # Example:

# from abc import ABC, abstractmethod

# class Animal(ABC):  # Abstract class
#         @abstractmethod
#         def make_sound(self):
#             pass  # Must be implemented by subclasses

# class Dog(Animal):
#         def make_sound(self):
#             print("Bark")

# dog = Dog()
# dog.make_sound()  # Output: Bark

#Here, Animal is an abstract class, meaning you cannot create an object from it directly. Only the child class (Dog) provides the full implementation.

#4. Encapsulation (Data Protection)

    #Definition: Encapsulation restricts access to certain details of an object to protect its integrity.

   # Analogy: A bank ATM only allows you to withdraw money through specific functions, but you can't directly access its internal database.

   # Example:

# class BankAccount:
#         def __init__(self, balance):
#             self.__balance = balance  # Private variable (cannot be accessed directly)

#         def deposit(self, amount):
#             self.__balance += amount

#         def get_balance(self):
#             return self.__balance

# account = BankAccount(1000)
# account.deposit(500)
# print(account.get_balance())  # Output: 1500

  #  The __balance variable is private, so it cannot be modified directly, ensuring data security.

#Quick Summary
#OOP Concept	Purpose	Example
##Polymorphism	Use a single interface for different types	Different classes can share the same method name but behave differently
#Abstraction	Hide complex details, expose only the necessary parts	Abstract classes and methods define a structure but leave details to child classes
#Encapsulation	Protect and restrict access to data	Private variables and getter/setter methods


