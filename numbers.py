# Integers

sum = 1 + 5
print(sum)
num1 = 1
num2 = 5
sum = num1 + num2
print(sum)

# Floats

float_sum = 5.5 + 1.5
print(float_sum)
float_sum1 = 5.5
float_sum2 = 1.5
float_sum = float_sum1 + float_sum2
print(float_sum)

# Type errors (use numbers in strings)
#  print("The sum of " + float_sum1 + " and " + float_sum2 + " is " + float_sum) ===> This line gives an error

print("The sum of " + str(float_sum1) + " and " + str(float_sum2) + " is " + str(float_sum)) #This one does not

# the number 8 exercise

print(5 + 3)
print(11 - 3)
print(24 / 3)
print(4 * 2)

# Favourite Number

favorite_number = 13
print("My favourite number is " + str(favorite_number))