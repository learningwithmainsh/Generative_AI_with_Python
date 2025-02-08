class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Method to calculate area
    def area(self):
        return self.width * self.height

    # Method to calculate perimeter
    def perimeter(self):
        # return 2 * (self.width * self.height)
        return 2 * (self.area())

    # Method to display both area and perimeter by calling methods
    def display_info(self):
        # Call area using self
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")

rectangle = Rectangle(10, 15)
rectangle.display_info()
