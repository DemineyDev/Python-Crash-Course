# List with three invitees, print message to each inviting them to dinner

invitees = ["Steve Jobs", "Bill Gates", "Monty Python"]

print(invitees[0] + ", please come to my dinner")
print(invitees[1] + ", please come to my dinner")
print(invitees[2] + ", please come to my dinner")

# One guest can't make it

print(invitees[0] + " can't make it anymore")

invitees[0] = "Mark Cuban"

print(invitees)

# Found a bigger table

print("We found a bigger table for the dinner party")
invitees.insert(0, "Tom Jones")
invitees.insert(1, "Elvis Presley")
invitees.append("Elton John")
print(invitees)

# Table won't arrive in time for dinner

print("The table did not arrive, only two people can come.")
print("Sorry, " + invitees.pop() + " you can't come anymore")
print("Sorry, " + invitees.pop() + " you can't come anymore")
print("Sorry, " + invitees.pop() + " you can't come anymore")
print("Sorry, " + invitees.pop() + " you can't come anymore")

print(invitees)

print(invitees[0] + " you can still come to the dinner")
print(invitees[1] + " you can still come to the dinner")

del invitees[0]
del invitees[0]

print(invitees)