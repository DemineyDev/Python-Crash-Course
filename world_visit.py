# Five places I would like to visit

places = ["Paris", "Vienna", "Prague", "Zurich", "Rome"]
print(places)

# Sort the list temporarily with sorted()
print(sorted(places))
# List still in original form
print(places)
# Sorted in reverse alphabetical order
print(sorted(places, reverse=True))
# List still in original form
print(places)
# reverse list with reverse()
places.reverse()
print(places)
# Reverse again
places.reverse()
print(places)

# Sort the list with sort()
places.sort()
print(places)

# Sort in reverse alphabetical order
places.sort(reverse = True)
print(places)

print(len(places))