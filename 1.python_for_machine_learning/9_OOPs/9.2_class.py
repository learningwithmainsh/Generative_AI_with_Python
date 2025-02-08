class Dog:
    # Constructor method to initialize an object
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print("Hi, I am awake")

    def display_info(self):
        print(f"My name is {self.name} and I am a {self.breed}")
    
    def bark(self):
        print(f"{self.name} says Woof!")

# Creating an instance outside the class definition
dog1 = Dog("Buddy", "Golden Retriever")
dog1.bark()
