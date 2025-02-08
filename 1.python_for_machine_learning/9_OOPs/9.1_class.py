# Difining the class
class Dog:
    # Constructor method to initialise an object
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


    def display_info(self):
        print(f"My name is {self.name} and I am a {self.breed}")

# Dog("buddy", "Golden")
    
dog1 = Dog("buddy", "Golden")
print(type(dog1))
print(dog1.name)
print(dog1.breed)
print(dog1.display_info())

