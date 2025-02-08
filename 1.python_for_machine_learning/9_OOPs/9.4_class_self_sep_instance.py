# Defining a class Employee to store employee details
class Employee:
    def __init__(self, name, salary):
        # Initializing employee name and salary attributes
        self.name = name
        self.salary = salary

    def give_raised(self, amount):
        # Increasing salary by the given amount
        self.salary += amount
        # Printing the updated salary
        print(f"{self.name}'s new salary is {self.salary}")

# Creating instances of Employee
emp1 = Employee("Alice", 58000)
emp2 = Employee("Bob", 58001)

# Giving a raise to employees
emp1.give_raised(1000)  # Alice's salary increased by 1000
emp2.give_raised(2000)  # Bob's salary increased by 2000

