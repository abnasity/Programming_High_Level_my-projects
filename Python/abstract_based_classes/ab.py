from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass
    
    def describe(self):
        """Return a description of the shape with its area and perimeter."""
        return f"This shape has an area of {self.area():.2f} and a perimeter of {self.perimeter():.2f}."

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def __str__(self):
        return f"Circle with radius {self.radius}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return f"Rectangle with width {self.width} and height {self.height}"

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
        self.side_length = side_length
    
    def __str__(self):
        return f"Square with side length {self.side_length}"

# Usage example
def print_shape_info(shape):
    """Function that works with any Shape subclass"""
    print(f"{shape}")
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")
    print(shape.describe())
    print()

# Create different shapes
circle = Circle(5)
rectangle = Rectangle(4, 6)
square = Square(4)

# The same function works with all shape types
print_shape_info(circle)
print_shape_info(rectangle)
print_shape_info(square)

# This would raise an error:
# shape = Shape()  # TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter
