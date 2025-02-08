class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"
    
class Bird:
    def speak(self):
        return "Chirp"
    
def animal_sound(animal):
    print(animal.speak())

#Using Duck typing
dog = Dog()
cat = Cat()
bird = Bird()

animal_sound(dog)
animal_sound(cat)
animal_sound(bird)



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # String representation of the object
    def __str__(self):
        return f"Point({self.x}, {self.y})"

# Creating two Point objects
p1 = Point(1, 2)
p2 = Point(3, 4)

# Using the + operator on Point objects
p3 = p1 + p2

# Printing the result
print(p3)  # Output: Point(4, 6)