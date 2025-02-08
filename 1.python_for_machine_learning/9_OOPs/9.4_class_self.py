class Car:
    # Constructor that initialise the instance attribute using self
    def __init__(self, make, model):
        self.make = make
        self.model = model


    # Method to display car Information
    def display_info(self):
        print(f"Care Make: {self.make},Model: {self.model}")

#Creating the instance of the Car class
car1 = Car("Toyota","Camry")
car2 = Car("Honda","Accord")

car1.display_info()
car2.display_info()
        

class Person:
    def __init__(self,name,age,):
        self.name = name
        self.age = age
    def birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}! You aren{self.age} year old.")


#creating an instance of Person
person1 = Person("Ram",30)
person2 = Person("Shyam",28)

print(f"Name:{person1.name}, Age:{person1.age}")
person1.birthday()
print(f"Name:{person1.name}, Age:{person1.age}")
print("**********")
print(f"Name:{person2.name}, Age:{person2.age}")