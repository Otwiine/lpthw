# Defines the cheese_and_crackers funtion
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# Uses numbers to give the function its values
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# Uses variables to feed the values in
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Uses math
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# Combines both variables and math
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# Study drills
def name(first, second):
    print(f"What is your first name?: {first}")
    print(f"What is your second name?: {second}")

name("Otwiine", "Olweny")

def fav_num(num1, num2):
    print(f"Your first favourite number is: {num1}")
    print(f"Your second favourite number is: {num2}")

fav_num(20, 50 % 30) # 20, 20

def numbers(number1, number2):
    print(f"This is number 1: {number1}")
    print(f"This is number 2: {number2}")

numbers(30 - 5, 78 / 7)