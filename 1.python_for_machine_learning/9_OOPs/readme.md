# Python Object-Oriented Programming (OOP)

## Introduction
Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to structure and manage code. Python supports OOP, allowing developers to create reusable and modular code.

## Key OOP Concepts in Python

### 1. Classes and Objects
- **Class**: A blueprint for creating objects.
- **Object**: An instance of a class.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_info(self):
        return f"Car: {self.brand} {self.model}"

car1 = Car("Toyota", "Corolla")
print(car1.display_info())
```

### 2. Encapsulation
Encapsulation is the bundling of data and methods that operate on that data within a class.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())
```

### 3. Inheritance
Inheritance allows a class to inherit methods and attributes from another class.

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        return f"Brand: {self.brand}"

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

car = Car("Honda", "Civic")
print(car.show_brand())
```

### 4. Polymorphism
Polymorphism allows different classes to define methods with the same name but different behaviors.

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def make_sound(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()
make_sound(dog)
make_sound(cat)
```

### 5. Abstraction
Abstraction hides implementation details and only exposes necessary functionalities.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark"

dog = Dog()
print(dog.make_sound())
```

## Conclusion
Python's OOP features help in writing organized, reusable, and scalable code. By understanding and applying OOP principles, developers can build efficient and maintainable applications.

## Further Reading
- [Python Official Documentation](https://docs.python.org/3/tutorial/classes.html)
