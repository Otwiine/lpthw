# Assigns the number of cars to the variable 'cars'
cars = 100

# Assigns the number of seats in a car to the variable 'space_in_a_car'
space_in_a_car = 4.0

# Assigns the number of drivers to the variable 'drivers'
drivers = 30

# Assigns the number of passengers to the variable 'passengers'
passengers = 90

# Calculates 'cars_not_driven' by subtracting 'drivers' from 'cars'
cars_not_driven = cars - drivers

# Assigns 'cars_driven' to the same value as 'drivers'
cars_driven = drivers

# Calculates 'carpool_capacity' by multiplying 'cars_driven' by 'space_in_a_car'
carpool_capacity = cars_driven * space_in_a_car

# Calculates 'average_passengers_per_car' by dividing 'passengers' by 'cars_driven'
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")