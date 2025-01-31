# python allows creating exception by inheriting from exception class
class NegativeNumberError(Exception):
    "Custom Exception for negative numbers"
    pass

def check_postive(number):
    if number < 0:
        raise NegativeNumberError("negative number are not allowed!")
    return number

try:
    number = int(input("Enter a positive number:"))
    check_postive(number)

except NegativeNumberError as e:
    print("Error :", e)