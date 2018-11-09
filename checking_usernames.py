current_users = ["John", "Steve", "Joan", "Jack", "Ben","Phillip"]
new_users = ["Barry", "Peter", "Jill", "John", "James", "Steve"]

for user in current_users:
    user.lower()

for user in new_users:
    user.lower()
    if user in current_users:
        print("Sorry, that username is taken")
    else:
        print("That username is available")