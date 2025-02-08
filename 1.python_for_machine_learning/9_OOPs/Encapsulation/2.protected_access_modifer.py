# Protected Access Modifier
class Animal:
    def __init__(self, species):
        self._species =species # protected attribute

class Dog(Animal):
    def __init__(self, species, breed):
        self.breed = breed
        super().__init__(species)

dog1 =Dog("Mammal","Labrador")
print(dog1.breed)
# print(dog1._species) # Accessible but not recommended




