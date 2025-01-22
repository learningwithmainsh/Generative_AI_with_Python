# Order of Parameter
# when combining default and non-default parameter, non-default parameter should bel listed first:
def order_item(item, quantity=1):
    print(f"Ordering {quantity} of {item}")

order_item(3)


'''
Variable Length Argument in Python
Variable-length arguments refer to a feature that allows a function to accept a variable number of arguments in Python
Variable-length arguments refer to a feature that allows a function to accept a variable number of arguments in Python. It is also known as the argument that can also accept an unlimited amount of data as input inside the function. There are two types in Python:
Non – Keyworded Arguments (*args)
Keyworded Arguments (**kwargs)
'''

#Non – Keyworded Arguments (*args)
def addition(*args):
    """Return any number of arguments"""
    print(sum(args))

addition(1,2,3)


# Keyworded Arguments (**kwargs)
def display_info(**kwargs):
    """Print user information passed as keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=30, city="New York")

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="manish",City="Pune", Company="Navadhan")


# Combining *args and **kwargs
def print_args_and_kwargs(*args, **kwargs):
	print("Positional arguments:")
	for arg in args:
		print(arg)
	
	print("Keyword arguments:")
	for key, value in kwargs.items():
		print(f"{key}: {value}")

print_args_and_kwargs(1, 2, 3, name="Alice", age=30)

def display_info(required,*args,**kwargs):
    print(f"Required argument: {required}")
    print(f"Additional arguments: {args}")
    print(f"Keyword agruments: {kwargs}")

display_info("mandatoray", "optional1","optional2",key1="value1",key2="value2")



"""Python return statement

A return statement is used to end the execution of the function call and it “returns” the value of the expression following the return keyword to the caller. 
The statements after the return statements are not executed. If the return statement is without any expression, then the special value None is returned. 
A return statement is overall used to invoke a function so that the passed statements can be executed."""

# Python return statement
def addition(*args):
    """Return any number of arguments"""
    return sum(args)


sum1 =(addition(1,2,3))
print(sum1)
sum2 = (addition(1,2,3,4))
print(sum2)

#example

def convert_temperature(temp, unit):
    """Convert temperature between Celsius and Fahrenheit."""
    if unit == "C":
        # Celsius to Fahrenheit
        return temp * 9 / 5 + 32
    elif unit == "F":
        # Fahrenheit to Celsius
        return (temp - 32) * 5 / 9
    else:
        # Invalid unit
        return None

# Test cases
print(convert_temperature(98.6, "F"))  # Output: 36.44444444444444
print(convert_temperature(100, "C"))  # Output: 212.0




