#define function
def func_name():
    print("Hello, I am first function of this module")

print("Endo of Function")

# call the function
func_name()

# Docstring
# Docstrings, short for documentation strings, are vital in conveying the purpose and functionality of Python functions, modules, and classes.

def add():
    """ Printing the Addtion of values """
    print(10+15)

add()

#function parameters python
#A parameter is the variable listed inside the parentheses in the function definition. An argument is the value that is sent to the function when it is called.

def sum(value1,value2):
    """ Printing the Addtion of values """
    print(value1 + value2)

sum(10,20)
sum(30,70)

#function default parameters python
#Python allows function arguments to have default values. If the function is called without the argument, the argument gets its default value.

def sum(value1=1,value2=2):
    """ Printing the Addtion of values """
    print(value1 + value2)

sum(10,20)
sum()
sum(50)