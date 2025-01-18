# creating tuple
my_tuple = (1,100,"Jame",30.4,True, (3,4,"Maria"),["list,python,11"])
print(type(my_tuple))
print(my_tuple)

#accessing the tuple
print(my_tuple[2])
print(my_tuple[-2])
print(my_tuple[:5])


#common methods:
#count(): return number of occurance
#index():return the index of number

numbers = (1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7)
print(numbers.count(2))
print(numbers.index(5))

# Converting List to Tuple and Tuple to List

# Initial list
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

# Convert list to tuple
converted_tuple = tuple(my_list)
print("Converted Tuple:", converted_tuple)

# Initial tuple
my_tuple = (6, 7, 8, 9, 10)
print("\nOriginal Tuple:", my_tuple)

# Convert tuple to list
converted_list = list(my_tuple)
print("Converted List:", converted_list)
