class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self, mileage):
        self.odometer_reading = mileage
        if mileage <= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer")


my_new_car = Car("renault", "duster", 2018)
my_new_car.read_odometer()

print(my_new_car.get_descriptive_name())

# Modify and attribute

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_new_car.update_odometer(55)
my_new_car.read_odometer()