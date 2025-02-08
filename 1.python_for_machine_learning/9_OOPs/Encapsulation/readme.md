# Encapsulation in Python

## Introduction
Encapsulation is one of the fundamental principles of Object-Oriented Programming (OOP). It refers to restricting direct access to some of an object's components, which can prevent the accidental modification of data. In Python, encapsulation is implemented using private and protected access modifiers.

## Access Modifiers in Python
Python provides three types of access modifiers:

1. **Public Members**: These members are accessible from anywhere.
2. **Protected Members (_variable)**: These members are indicated with a single underscore and should not be accessed directly outside the class, though they are not strictly private.
3. **Private Members (__variable)**: These members are indicated with double underscores and cannot be accessed directly outside the class.

## Example of Encapsulation
```python
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public member
        self._bank_name = "Secure Bank"  # Protected member
        self.__balance = balance  # Private member
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. Remaining balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")
    
    def get_balance(self):
        return self.__balance

# Creating an object of BankAccount class
account = BankAccount("John Doe", 1000)
print(account.account_holder)  # Accessible (Public)
print(account._bank_name)  # Accessible but should be treated as protected

# Trying to access private attribute directly
# print(account.__balance)  # This will raise an AttributeError

# Accessing private variable using name mangling
print(account._BankAccount__balance)  # This works but is not recommended
```

## Benefits of Encapsulation
- **Data Hiding**: Prevents direct modification of sensitive data.
- **Code Maintainability**: Reduces complexity by defining clear access rules.
- **Improved Security**: Protects the integrity of the object’s data.

## Best Practices
- Use getter and setter methods to access private attributes.
- Follow naming conventions for public, protected, and private members.
- Avoid using name mangling unless absolutely necessary.

## Conclusion
Encapsulation is a key concept in Python's OOP paradigm that enhances security, maintainability, and clarity in code. By properly using access modifiers, developers can ensure controlled access to class attributes and methods.

