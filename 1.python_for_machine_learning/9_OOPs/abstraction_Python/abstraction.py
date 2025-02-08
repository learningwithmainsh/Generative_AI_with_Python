import math
from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Rectangle class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

# Creating instances
rect = Rectangle(5, 3)
circle = Circle(4)

# Outputting results
print(f"Rectangle - Area: {rect.area()}, Perimeter: {rect.perimeter()}")
print(f"Circle - Area: {circle.area()}, Perimeter: {circle.perimeter()}")
