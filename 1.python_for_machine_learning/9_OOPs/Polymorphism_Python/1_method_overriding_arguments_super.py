class Animal:
    def speak(self, sound):
        print(f"Animal makes a sound: {sound}")

class Dog(Animal):
    def speak(self, sound, name):
        # Calling the parent class method using super()
        super().speak(sound)
        print(f"{name} the dog barks: {sound}")

# Create an instance of Dog
dog = Dog()

# Call the overridden method
dog.speak("Woof!", "Buddy")
