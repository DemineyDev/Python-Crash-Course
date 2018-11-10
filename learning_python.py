filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()


for item in lines:
    print(item)

with open(filename) as file_object:
    contents = file_object.read()

print(contents)

print(contents.replace('Python', 'C#'))

print(contents)