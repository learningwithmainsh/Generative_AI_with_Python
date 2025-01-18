person = {"name":"manish","age":30,"role":"engineer"}
print(person)
print(type(person))

print("******")

mixed_dict = {"name":"alice","age":25, 1:[1,2,3,4,5]}
print(mixed_dict)

#accessing element in dict
person1 = {"name":"manish","age":30,"role":"engineer","city":"pune"}
print(person1["city"])
print(person1.get("city"))
print(person1.get("cities")) # will not get errors if key not exist
print(person1.get("cities", "key Missing ,Defaut is Pune")) # get default value

# modified dict

person1 = {"name":"manish","age":30,"role":"engineer","city":"pune"}
person1["city"] = "Delhi"
print(person1)

#adding value in Dictionary
person1["number"]=123456
print(person1)

#remove key value pair
del person1["age"]
print(person1)

#removing key using pop() function
print(person1.pop("role"))
print("********")
print(person1)

