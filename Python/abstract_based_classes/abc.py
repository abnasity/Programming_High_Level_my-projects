from abc import ABC

class Fruit(ABC):

    def have_seed(self):
        pass
    def seed_color(self):
        pass
    
class Apple(Fruit):
    
    def __init__(self):
        self.seed = True
        self.color = "Red"
        
    def have_seed(self):
        return self.seed
    
    def seed_color(self):
        return self.color
apple = Apple()
print(apple.have_seed())
apple = Apple()
print(apple.seed_color())