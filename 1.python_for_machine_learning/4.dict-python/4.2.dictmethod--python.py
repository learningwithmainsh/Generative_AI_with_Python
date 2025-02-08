person = {"name":"manish","age":30,"role":"engineer","city":"pune"}
print(person.keys())
print(person.values())
print(person.items())
print(person)

print("__________")
for item in person.values():
    print(item)

#updating value in dict
print("______________")
person.update({"country":"USA","Citizen":"Yes"})
print(person)

#removing values fro dict
# print("___________________")
# person.clear()
# print(person)

# iterating over Dictionaries
for key in person.keys():
    print(key)
print("______________")

for value in person.values():
    print(value)
print("______________")

for item in person.items():
    print(item)
print("______________")



