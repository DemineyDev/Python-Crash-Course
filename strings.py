new_string = ("This is a string")
print(new_string)

# Capitalize the first letters of the words

name = "deminey dev"
print(name.title())

# change all the letters to uppercase

print(name.upper())

# and then lower

print(name.lower())

#string concatenation

first_name = "Deminey"
last_name = "Dev"

full_name = first_name + " " + last_name
print(full_name)
print("Hello " + full_name)

# Add a teb next to your text

print("\tPython")
print("\t"+ full_name)

# Add a new line in your string

print("Languages:\n\tPython\n\tJavascript\n\tC#")

# Remove white space from a string

user = "Deminey Dev   "
print(user.rstrip())

# Syntax error with apostrophe

message = "One of Python's strengths is its diverse community" # no error message. If it was single quotes an error message would have been displayed

print(message)

# exercises

person_name = "John"
print ("Hello " + person_name)

print(person_name.upper())
print(person_name.lower())
print(person_name.title())

famous_quote = 'Albert Einstein once said, "A person who never made a mistake never tried anything new."'
print(famous_quote)

famous_person = "Albert Einstein"
famous_person_quote = '"A person who never made a mistake never tried anything new"'
famous_message = famous_person + " once said, " + famous_person_quote
print(famous_message)