# Assigning the variables values
people = 45
cars = 20
trucks = 13

# Checks if cars are greater than people
if cars > people:
    print("We should take the cars.")
# Checks if cars are less than people
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

# Checks if trucks are greater than cars
if trucks > cars:
    print("That's too many trucks.")
# Checks if trucks are less than cars
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if cars > people or trucks < cars:
    print("Let's use the trucks.")

# Checks if people are greater than trucks
if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")