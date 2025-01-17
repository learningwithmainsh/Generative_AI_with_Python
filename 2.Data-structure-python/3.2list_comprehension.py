#nested list comprehesion
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
pair_list = [[i, j] for i in list1 for j in list2]
print(pair_list)

print("newline")

# nested list 
mixed_list = [1,2,3,4,5,["manish","kumar","Pandey"]]
print(mixed_list[3])
print(mixed_list[5])
print(mixed_list[5][0])

