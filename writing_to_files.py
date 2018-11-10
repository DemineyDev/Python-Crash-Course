filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in big data!\n")
    file_object.write(("I love doing machine learning\n"))
