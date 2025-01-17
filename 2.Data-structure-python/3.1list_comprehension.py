# List Comprehension in Python
# List comprehensions provide a concise way to create lists.
# It consists of brackets containing an expression followed by a for clause, and optionally, one or more if clauses.

# Example 1: Create a list of squares for numbers 1 through 10.
squares = [x**2 for x in range(1, 11)]  # Using list comprehension to compute squares
print("Squares:", squares)

print("newline")
square = [y**2 for y in range (1,5)]
print("square", square)

#another example
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
updated_number = [i + 20 for i in numbers]
print("updated_number1:",updated_number)

#another example
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
updated_number = [i + 20 for i in numbers if i%2==1]
print("updated_number2:",updated_number)

#another example for checking square
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
updated_number = [i**2 for i in numbers if i%2==1]
print("updated_number3:",updated_number)


# Example 2: Create a list of even numbers from 1 to 20.
even_numbers = [x for x in range(1, 21) if x % 2 == 0]  # Filter condition to include only even numbers
print("Even Numbers:", even_numbers)

# Example 3: Convert a list of temperatures from Celsius to Fahrenheit.
temperatures_celsius = [0, 10, 20, 30, 40]  # List of temperatures in Celsius
temperatures_fahrenheit = [(c * 9/5) + 32 for c in temperatures_celsius]  # Conversion formula
print("Temperatures in Fahrenheit:", temperatures_fahrenheit)

# Example 4: Create a list of tuples containing numbers and their cubes for numbers 1 through 5.
number_cubes = [(x, x**3) for x in range(1, 6)]  # Creating tuples of number and its cube
print("Number and Cubes:", number_cubes)

# Example 5: Flatten a nested list into a single list.
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Nested list
flattened_list = [item for sublist in nested_list for item in sublist]  # Flattening the nested list
print("Flattened List:", flattened_list)

# Example 6: Filter words with more than 3 letters from a list of words.
words = ["apple", "an", "banana", "cat", "dog"]  # List of words
long_words = [word for word in words if len(word) > 3]  # Filtering words with length > 3
print("Words with more than 3 letters:", long_words)

# Example 7: Create a new list by applying conditional logic.
numbers = [-10, -5, 0, 5, 10]  # List of numbers
# Replace negative numbers with 0, keep other numbers as is
transformed_numbers = [0 if x < 0 else x for x in numbers]  # Conditional logic in list comprehension
print("Transformed Numbers:", transformed_numbers)
