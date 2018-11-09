users = ["John", "Steve", "Peter", "Suzy", "admin"]

for user in users:
    if len(users) <= 0:
        print("We need to find some users")
    else:
        if user == "admin":
            print("Hello admin, would you like to see a status report")
        else:
            print("Hello User, welcome to the system")