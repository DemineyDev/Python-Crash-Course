nums = list(range(1,31))
print("The first three items in the list are:")
print(nums[0:3])
print("The middle three items in the list are:")
print(nums[14:17])
print("The last three items of the list are:")
print(nums[-3:])


pizzas = ["Pepperroni", "Ham", "Mushrooms", "Garlic"]
friends_pizza = pizzas[:]
friends_pizza.append("Russian")
pizzas.append("Chilli")

print(pizzas)
print(friends_pizza)

for pizza in pizzas:
    print(pizza)