# Number of cars 
cars = 100
# Space in each car
space_in_a_car = 4.0
# Number of drivers
drivers = 30
# Number of passengers
passengers = 90
# Number of empty cars
cars_not_driven = cars - drivers
# Number of cars driven
cars_driven = drivers
# Amount of people that can be carpooled
carpool_capacity = cars_driven * space_in_a_car
# Average amoun tof passengers per car
average_passengers_per_car = passengers / cars_driven

# Prints the statements using data stored in the variables
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")