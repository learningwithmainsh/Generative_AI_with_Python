# raise statement let you trigger exceptions manually.
# It is useful for validating data and debugging
def division(a,b):
    if b == a:
        raise ZeroDivisionError("You tried to divide by zero!")
    return a/b

try:
    print(division(10,2))
except ZeroDivisionError as e:
    print("Error:",e)