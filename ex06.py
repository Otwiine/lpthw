# Define a variable and assign it a variable of 10
types_of_people = 10

# Insert the variable into a new string which we assign to the variable 'x'
x = f"There are {types_of_people} types of people"

# Define a variable 'binary' the string binary
binary = "binary"

# Define a variable 'do_not' the string don't
do_not = "don't"

# Embed those two string variables into a new string and assign it to the variable y
y = f"Those who know {binary} and those who {do_not}"

# Print the value of 'x' and 'y' variables
print(x)
print(y)

# We print the value for 'x' and 'y' variables, using an f-string
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Assign a boolean value to a variable
hilarious = False

# Assign a new string variable with a placeholder
joke_evaluation = "Isn't that joke so funny so funny?! {}"

# Print out the value of the 'joke_evaluation', using format and passing the 'hilaroius' variable into it
print(joke_evaluation.format(hilarious))

# Assign a new variable w and e and assign strings to them
w = "This is the left side of..."
e = "a string with a right side."

# Print out a new string by concatenating the variables w and e
print(w + e)