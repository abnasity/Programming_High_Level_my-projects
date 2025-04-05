#Types of polymorphism
#1)Dynamic polymorphism
#2)Operator overloading
#3)Method Overriding
#4)Method overloading


#Dynamic polymorphism
#

class Duck:
    def sound(self):
        print("Quack!")

class Cat:
    def sound(self):
        print("Meow!")

def make_sound(animal):  # No need to check type
    animal.sound()

duck = Duck()
cat = Cat()

make_sound(duck)  # ✅ Output: Quack!
make_sound(cat)   # ✅ Output: Meow!

#
