# Import argv from the sys module
from sys import argv

# Unpack the command-line arguments
script, input_file = argv

# Define a function that prints the entire file
def print_all(f):
    print(f.read())

# Define a function that takes the cursor back to the zero byte
def rewind(f):
    f.seek(0)

# Define a function that prints a specific line in the file
def print_a_line(line_count, f):
    print(line_count, f.readline())

# Open the file and store the file object in in current_file
current_file = open(input_file)

print("First let's print the whole file:\n")

# Print the contents of the entire file 
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

# Sets current_line and prints that line
current_line = 1
print_a_line(current_line, current_file)

# Prints lines 1 - 3 using print_a_line
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)