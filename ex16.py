# Imports the argv from the sys module (to handle command-line arguments)
from sys import argv
# Unpacks argv into two variables
script, filename = argv

# Prints out intentions using an f-string
print(f"We're going to erase {filename}.")
# Prompts the user to either abort or continue
print(f"If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
# Prompts the user for an input (Waits)
input("?")

# Prints the string
print("Opening the file...")
# Opens {filename} in write mode and stores it in the file object 'target'
target = open(filename, 'w')

# NOTE Opening a file in 'w' write mode truncates the file if it exists

# Prints the string
print("Truncating the file. Goodbye!")
# Empties the file by using .truncate on the file object 
target.truncate()

# Prints the string
print("Now I'm going to ask you for three lines.")

# Asks user for input and stores in the variables
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# Prints the string
print("I'm going to write these to the file.")

# Uses .write on the file object to write the lines stored in the variables to the file
# Also uses newline characters to go to the next line
target.write(f"{line1}+\n+{line2}+\n+{line3}+\n")

# Prints a message
print("And finally, we close it.")
# Close file to save changes and free up memory
target.close


# SCRIPT TO READ FILE
# script, filename = argv
# print(f"Let's read {filename}")
# file = open(filename)
# print(file.read())
# file.close()