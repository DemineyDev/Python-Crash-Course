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


# Create an instance of the class

my_dog = Dog('Willie', 6)

print ("My dog's name is " + my_dog.name.title())
print ("My dog is " + str(my_dog.age) + "years old")

wifes_dog = Dog('Jonie', 2)

print ("My dog's name is " + wifes_dog.name.title())
print ("My dog is " + str(wifes_dog.age) + "years old")

my_dog.sit()

my_dog.roll_over()