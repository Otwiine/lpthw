# Define a variable and assign it the value 10
types_of_people = 10
# Insert the variable into a new string which we assign to the variable x
x = f"There are {types_of_people} types of people."

# Define a variable with the string "binary"
binary = "binary"
# Define a variable with the string "don't"
do_not = "don't"
# Embed the string variables into a new string and assign it to a variable y
y = f"Those who know {binary} and those who {do_not}."

# Prints the x and y variables
print(x)
print(y)

# Prints x and y  variables in new strings, using an f" string
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Assigns the Boolean value False to the Hilarious variable
hilarious = False
# Defines a new string variablw ith a placeholder
joke_evaluation = "Isn't that joke so funny?! {}"

# Print out the value of joke_evaluation using .format to pass the hilarious Boolean variable into it
print(joke_evaluation.format(hilarious))

# Define new variables w and e and assign strings to them
w = "This is the left side of..."
e = "a string with a right side."

# Print out a new string by concatenating the variables w and e
print(w + e)