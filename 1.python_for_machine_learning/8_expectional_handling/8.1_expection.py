def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        result = None
    except TypeError:
        print("Error: Invalid input type. Please provide numbers.")
        result = None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        result = None
    else:
        print("Division successful.")
    finally:
        print("Execution completed.")
    
    return result


a = 10
b = 0
print("Result:", divide_numbers(a, b))


def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        result = None
    except TypeError:
        print("Error: Invalid input type. Please provide numbers.")
        result = None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        result = None
    else:
        print("Division successful.")
    finally:
        print("Execution completed.")
    
    return result


try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    print("Result:", divide_numbers(numerator, denominator))
except ValueError:
    print("Error: Invalid input. Please enter numerical values.")
