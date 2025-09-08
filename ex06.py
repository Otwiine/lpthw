# Assigns 10 to types_of_people
types_of_people = 10
# Assigns an f-string to the variable x
x = f"There are {types_of_people} types of people."

# Assigns strings to the variables
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# Prints out the variables
print(x)
print(y)

# Prints out variables using f-strings
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Assigns a boolean value to the variable hilarious
hilarious = False
# Assigns a string with a placeholder to the joke_eval variable 
joke_evaluation = "Isn't that joke so funny?! {}"

# Inserts the boolean value of 'hilarious' into the string using .format()
print(joke_evaluation.format(hilarious))

# Assigns text to the variables w and e
w = "This is the left side of..."
e = "a string with a right side."

# Concatenates the two string variables
print(w + e)