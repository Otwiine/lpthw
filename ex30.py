# Assigns values to the variables
people = 30
cars = 40
trucks = 15

# Check if number of cars is greater than people 
if cars > people:
    print("We should take the cars.")
# check if number of cars is less than people
elif cars < people:
    print("We should not take the cars.")
# Print this if neither condition is true
else:
    print("We can't decide.")

# Check if number of trucks is  greater than number of cars
if trucks > cars:
    print("That's too many trucks.")
# Check if number of trucks is less than number of cars
elif trucks < cars:
    print("Maybe we could take the trucks.")
# Print this if neither condition is true
else:
    print("We still can't decide.")

# Check if number of people is greater than number of trucks
if people > trucks:
    print("Alright, let's just take the trucks.")
# Print this if the condition is not met
else:
    print("Fine, let's stay home then.")

# if cars > people and trucks < cars:
#     print("Lets use the cars")
# elif cars < people and trucks < people:
#     print("We're walking")