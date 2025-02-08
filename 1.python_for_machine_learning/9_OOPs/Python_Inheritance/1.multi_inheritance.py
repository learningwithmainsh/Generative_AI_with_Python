
#Multi_inheritance
#Example 1
class Teacher:
    def teach(self):
        return "Teaching Subjects."
class SportCoach:
    def coach(self):
        return "Coaching Sports"

class SchoolStaff(Teacher,SportCoach):
    def manage(self):
        return "Managing School Activities"

#Testing multi inheritance
staff =SchoolStaff()
print(staff.manage())
print(staff.coach())
print(staff.teach())


#Multiinheritence
print("***********")
# Base class
class Animal:
    def speak(self):
        print("Animal speaks")

# Derived class from Animal
class Mammal(Animal):
    def walk(self):
        print("Mammal walks")

# Derived class from Mammal
class Dog(Mammal):
    def bark(self):
        print("Dog barks")

# Create an object of Dog
dog = Dog()

# Calling methods from all levels of inheritance
dog.speak()  # Method from Animal class
dog.walk()   # Method from Mammal class
dog.bark()   # Method from Dog class


print("*********")

class A:
    def message(self):
        return "Message from A"

class B:
    def message(self):
        return "Message from B"   

class C(A):
    def message(self):
        return "Message from C"
class D(B,C):
    pass

# Testing daimaond problem reslotution
#        
d =D()
print(d.message())
print(D.mro())

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary

    def display_employee_info(self):
        print(f"Employee ID: {self.emp_id}, Salary: {self.salary}")

# Teacher inherits from both Person and Employee
class Teacher(Person, Employee):
    def __init__(self, name, age, emp_id, salary, subject):
        # Calling constructors of both parent classes
        Person.__init__(self, name, age)
        Employee.__init__(self, emp_id, salary)
        self.subject = subject

    def display_teacher_info(self):
        self.display_person_info()
        self.display_employee_info()
        print(f"Subject: {self.subject}")

# Creating an object of Teacher
teacher1 = Teacher("John Doe", 35, "T123", 50000, "Mathematics")

# Displaying Teacher details
teacher1.display_teacher_info()
