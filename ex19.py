# Define a function that prints info about cheese and crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# Call the funtion using nubers directly
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# Define variables and pass them to the function
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Use math expressions as arguments
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5+ 6)

# Combine variables and math in the function call
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)