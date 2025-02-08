# main.py
import customMath
from customShapes import Circle, Rectangle

# Using customMath module
print("Sum:", customMath.add(10, 5))
print("Difference:", customMath.subtract(10, 5))

# Using Circle class
circle = Circle(7)
print("Area of circle is:", circle.area())
print("Circumference of circle is:", circle.circumference())

# Using Rectangle class
rectangle = Rectangle(10, 20)
print("Area of rectangle is:", rectangle.area())
print("Perimeter of rectangle is:", rectangle.perimeter())
