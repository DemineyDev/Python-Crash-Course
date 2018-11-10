# Create Class

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("This restaurant's name is " + self.restaurant_name)
        print("This restaurant serves " + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + " is open")


# Create instance of class

restaurant = Restaurant("Godfather", "Steak")

restaurant.describe_restaurant()
restaurant.open_restaurant()

italian_restaurant = Restaurant("Lupa", "Italian")

take_away_restaurant = Restaurant("McDonalds", "Take-Aways")

italian_restaurant.describe_restaurant()

take_away_restaurant.describe_restaurant()