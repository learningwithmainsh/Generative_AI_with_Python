class Animal:
    def speak(self, sound="..."):
        print(f"The animal makes a sound: {sound}")

class Dog(Animal):
    # Overriding the speak method with an additional argument
    def speak(self, sound="bark", times=1):
        print(f"The dog says: {(sound + ' ') * times}")

# Creating instances
generic_animal = Animal()
dog = Dog()

# Calling methods
generic_animal.speak()              
generic_animal.speak("growl")        

dog.speak()                          
dog.speak("woof", 3)                 
