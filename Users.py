class Users:
    def __init__(self, first_name, last_name):
        self.firstname = first_name
        self.lastname = last_name

    def describe_user(self):
        print("The users first name is " + self.firstname)
        print("The users last name is " + self.lastname)

    def greet_user(self):
        print ("Hello " + self.firstname + ", how are you?")

user1 = Users("Steve", "Jobs")
user2 = Users("Bill", "Gates")
user3 = Users("Tom", "Jones")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()