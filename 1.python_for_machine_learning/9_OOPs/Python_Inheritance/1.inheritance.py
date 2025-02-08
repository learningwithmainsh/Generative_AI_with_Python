# Company has general employees and specialized roles: Developer and Manager

# Base class for all employees
class Employee:
    def __init__(self, name, salary):
        """
        Initializes an Employee with a name and salary.
        """
        self.name = name
        self.salary = salary
    
    def get_details(self):
        """
        Returns a string with the employee's details.
        """
        return f"Name: {self.name}, Salary: ${self.salary}"

# Developer class inheriting from Employee
class Developer(Employee):
    def __init__(self, name, salary, programming_languages):
        """
        Initializes a Developer with a name, salary, and a list of programming languages.
        Calls the Employee constructor to initialize common attributes.
        """
        super().__init__(name, salary)  # Call parent constructor
        self.programming_languages = programming_languages  # Additional attribute for Developer
    
    def get_details(self):
        """
        Returns a string with developer details including programming languages.
        """
        base_details = super().get_details()  # Get base class details
        return f"{base_details}, Programming Languages: {', '.join(self.programming_languages)}"

# Manager class inheriting from Employee
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        """
        Initializes a Manager with a name, salary, and team size.
        Calls the Employee constructor to initialize common attributes.
        """
        super().__init__(name, salary)  # Call parent constructor
        self.team_size = team_size  # Additional attribute for Manager
     
    def get_details(self):
        """
        Returns a string with manager details including team size.
        """
        base_details = super().get_details()
        return f"{base_details}, Team Size: {self.team_size}"

# Creating an instance of Developer
dev = Developer("Alice", 8000, ["Python", "Go"])
print(dev.get_details())  # Prints developer details

# Creating an instance of Manager
mgr = Manager("Bob", 90000, 10)
print(mgr.get_details())  # Prints manager details
