# Number of Cars
cars = 100
# Seeats in the car
space_in_a_car = 4.0
# Number of drivers
drivers = 30
# Total passengers
passengers = 90
# Empty cars
cars_not_driven = cars - drivers
# Cars used
cars_driven = drivers
# Max capacity of people that can be taken
carpool_capacity = cars_driven * space_in_a_car
# Average number of passengers per car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people taday.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")