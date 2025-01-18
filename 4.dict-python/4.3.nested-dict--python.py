company = {
    "emp1":{"name":"alice","age":34,"role":"eng"},
    "emp2":{"name":"alice1","age":34,"role":"eng2"}
}

print(company)
print(company.keys())
print(company.values())
print(company.items())

print("_________")
print(company["emp1"])
print(company["emp1"]["role"])