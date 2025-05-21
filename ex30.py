# Assigns value to the variables representing the number of people, cars and trucks
people = 30 
cars = 40
trucks = 15

# Decide whether to take the cars based on their number relative to people
if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

# Evaluate the number of trucks compared to cars to help make a decision
if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still cant decide.")

# Make a final decision based on the number of people versus trucks
if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")