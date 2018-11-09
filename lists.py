# simple list

bicycles = ["Cannondale", "Trek", "Giant", "Specialized", "Titan", "Redline"]
print(bicycles)

# Accessing items in a list

print(bicycles[0])
print(bicycles[1])
print(bicycles[2])
print(bicycles[3])
print(bicycles[4])
print(bicycles[5])

# Format items in a list

print(bicycles[0].upper())
print(bicycles[3].lower())

# Accessing items from the back

print(bicycles[-1])
print(bicycles[-2])
print(bicycles[-3])

# Using individual values from a list

print("My first bicycle was a " + bicycles[3])

# Changing, adding and removing items from a list

motorcycles = ["Honda", "Suzuki", "Kawasaki", "Yamaha"]
print(motorcycles)
motorcycles[0] = "Ducati" # Changes the item in the list
print(motorcycles)
motorcycles.append("Honda") # The item is added to the end of the list
print(motorcycles)

cars = []
cars.append("BMW")
cars.append("Mercedes")
cars.append("Toyota")
cars.append("Audi")
print(cars)

# Insert Elements into a list

cars.insert(0, "Toyota")
print(cars)

# Removing Elements from a list

del cars[0] # using del
print(cars)

cars.pop() # Using pop
print(cars)

cars.remove("BMW")
print(cars)