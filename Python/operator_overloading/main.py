#operator overloading
#addition and subtraction to extract two points of a coordinate 
class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # Overloading '+'
        return Coordinates(self.x + other.x, self.y + other.y)
    
    def __sub__(self, another):
        return Coordinates(self.x - another.x, self.y - another.y )
        

p1 = Coordinates(2, 3)
p2 = Coordinates(4, 5)
p4 = Coordinates(7, 1)
p3 = p1 + p2  # Calls __add__()
p4 = p4 - p2  #calls __sub__()

# print(f"({p2.x}, {p2.y})")
print(f"({p3.x}, {p3.y})")  # Output: (6, 8)
