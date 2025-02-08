# Importing the math module (currently unused)
# import math  

class Circle:
    # Defining a class-level constant for PI (approximate value)
    PI = 3.14444  

    def __init__(self, radius: float):
        """
        Constructor to initialize a Circle object with a given radius.
        :param radius: Radius of the circle
        """
        self.radius = radius  

    def area(self) -> float:
        """
        Method to calculate the area of the circle.
        :return: Area of the circle using the formula π * r^2
        """
        # Alternative ways to compute area (commented out)
        # return math.pi * (self.radius ** 2)  # Using math.pi for more accuracy
        # return 3.14 * (self.radius ** 2)  # Using a simpler approximation of π
        
        return Circle.PI * (self.radius ** 2)  # Using class-level PI value

# Creating instances of Circle with different radii
circle1 = Circle(10)
circle2 = Circle(11)
circle3 = Circle(12)

# Printing the area of each circle
print(circle1.area())  
print(circle2.area())  
print(circle3.area())  

# Printing formatted area values with radius details
print(f"Area of circle with radius {circle1.radius} is: {circle1.area()}")  
print(f"Area of circle with radius {circle2.radius} is: {circle2.area()}")  
print(f"Area of circle with radius {circle3.radius} is: {circle3.area()}")  

# Printing formatted area values with two decimal precision
print(f"Area of circle1: {circle1.area():.2f}")  
print(f"Area of circle2: {circle2.area():.2f}")  
print(f"Area of circle3: {circle3.area():.2f}")  

# Accessing the class variable PI from different instances
print(circle1.PI)  
print(circle2.PI)  
