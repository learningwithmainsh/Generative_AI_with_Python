# Method overriding
class Vehicle:
    def move(self):
        return "The vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "The Car is driving on the road"
    
class Bike(Vehicle):
    def move(self):
        return "The bike is pedaling"

# Create instance of each class
vehicle = Vehicle()
car = Car()
bike = Bike()

# Call the move method
print(vehicle.move()) 
print(car.move())
print(bike.move())
