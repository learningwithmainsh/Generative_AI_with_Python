# Public Access Modifie

class Car:
    def __init__(self, brand):
        self.brand = brand  # public attribute

car = Car("Toyota")  # Create an instance of Car
print(car.brand)  # Access the public attribute
