class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Coordinates(self.x + other.x, self.y + other.y)
    
    def __sub__(self, another):
        return Coordinates(self.x - another.x, self.y - another.y)
    
point1 = Coordinates(2,3)
point2 = Coordinates(3,4)
point3 = point1 + point2
point4 = point2 - point1
print(f"({point3.x},{point3.y})")
print(f"({point4.x},{point4.y})")
       