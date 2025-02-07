# Define the 'cheese_and_crackers' function with 2 parameters
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# Call our function with numbers as arguments
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# Define two variables and assign them numbers
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# Call our funtion with variables as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Call our funtion and pass calculations as arguments
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# Call our funtion and pass calculations with variables and integers
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that are sent to the function when it is called.


#STUDY DRILLS

# Using input
def age_sum():
    age1 = int(input("Age 1: "))
    age2 = int(input("Age 2: "))
    print(f"Age sum is", age1 + age2)

age_sum()

# Using arguments
def age_sum_2(age1, age2):
    print("Here is age 1:", age1)
    print("Here is age 2:", age2)
    print("Here is the total:", age1 + age2)
    print("\n")

age_1 = 54
age_2 = 45

age_sum_2(23, 56)
age_sum_2(age_1 + 46, 55 + age_2)
age_sum_2(age_1, age_2)
age_sum_2(age_1, age_2 - 12)
age_sum_2(500 - age_1, age_2 )
age_sum_2(45 - 22, 56 - 21)
age_sum_2(22 -12, 9 + 2)
age_sum_2(2 * 3, 4 * 4)
age_sum_2(50 / 2, 75 / 3)
age_sum_2(100 / 4 , 27 * 2)