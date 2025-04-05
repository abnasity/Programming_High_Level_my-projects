
class Duck:
    def sound(self):
        print("quacks")
    
class Cat:
    def sound(self):
        print("meows")
    
def make_sound(animal):
        animal.sound()
        
duck = Duck()
cat = Cat()

make_sound(duck)
make_sound(cat)


