# Imports argv from the sys module
from sys import argv
# read the WYSS section for how to run this
# unpacks argv
script, first, second, third = argv

# Print the script name and the three command-line arguments
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# Uses input to get user input
fourth = input("What is your last variable? ")
print("Your fourth variable is:", fourth)