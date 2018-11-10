# Create a class for a dog

class Dog():
    def __init__(self, name, age):
        # Initialize name and age attributes
        self.name = name
        self.age = age

    def sit(self):
        # Simulate a dos sitting in response to a command
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        #Simulate a dog roling over on command
        print(self.name.title() + " rolled over!")

