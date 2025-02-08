# Python Inheritance

## Introduction
Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (child class) to inherit attributes and methods from another class (parent class). This promotes code reusability and enhances the organization of the code.

## Types of Inheritance
Python supports different types of inheritance:

1. **Single Inheritance**: A child class inherits from a single parent class.
2. **Multiple Inheritance**: A child class inherits from multiple parent classes.
3. **Multilevel Inheritance**: A child class inherits from another child class.
4. **Hierarchical Inheritance**: Multiple child classes inherit from a single parent class.
5. **Hybrid Inheritance**: A combination of different types of inheritance.

## Example Usage
### 1. Single Inheritance
```python
class Parent:
    def func1(self):
        print("This is a function from the Parent class.")

class Child(Parent):
    def func2(self):
        print("This is a function from the Child class.")

# Creating an object of the Child class
obj = Child()
obj.func1()  # Accessing parent class method
obj.func2()
```

### 2. Multiple Inheritance
```python
class Parent1:
    def func1(self):
        print("This is from Parent1 class.")

class Parent2:
    def func2(self):
        print("This is from Parent2 class.")

class Child(Parent1, Parent2):
    def func3(self):
        print("This is from Child class.")

obj = Child()
obj.func1()
obj.func2()
obj.func3()
```

### 3. Multilevel Inheritance
```python
class Grandparent:
    def func1(self):
        print("This is from Grandparent class.")

class Parent(Grandparent):
    def func2(self):
        print("This is from Parent class.")

class Child(Parent):
    def func3(self):
        print("This is from Child class.")

obj = Child()
obj.func1()
obj.func2()
obj.func3()
```

### 4. Hierarchical Inheritance
```python
class Parent:
    def func1(self):
        print("This is from Parent class.")

class Child1(Parent):
    def func2(self):
        print("This is from Child1 class.")

class Child2(Parent):
    def func3(self):
        print("This is from Child2 class.")

obj1 = Child1()
obj2 = Child2()

obj1.func1()
obj1.func2()

obj2.func1()
obj2.func3()
```

### 5. Hybrid Inheritance
```python
class A:
    def func1(self):
        print("This is from class A.")

class B(A):
    def func2(self):
        print("This is from class B.")

class C(A):
    def func3(self):
        print("This is from class C.")

class D(B, C):
    def func4(self):
        print("This is from class D.")

obj = D()
obj.func1()
obj.func2()
obj.func3()
obj.func4()
```

## Method Resolution Order (MRO)
In multiple inheritance, Python follows a specific method resolution order (MRO) to determine the method to be executed first. You can check the MRO using:
```python
print(D.mro())
```

## Conclusion
Inheritance in Python is a powerful feature that enhances code reusability and hierarchy structure in applications. Understanding different types of inheritance helps in designing better object-oriented systems.

### Happy Coding! 🎯

