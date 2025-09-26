# Import argv from the sys module
from sys import argv

# Unpack argv (Assign cmd line arguments to variables)
script, input_file = argv

# Define print_all function 
def print_all(f):
    print(f.read())

# Define rewind function that uses seek(0) to reset the file pointer to the beginning
def rewind(f):
    f.seek(0)

# Print out line_count along with the line based on the pointer position
def print_a_line(line_count, f):
    print(line_count, f.readline())

# Open file and assign the file object to current_file
current_file = open(input_file)

# Print out the string
print("First let's print the whole file:\n")

# Use print all to print the contents of the file
print_all(current_file)

# Print the string
print("Now let's rewind, kind of like a tape.")

# Return to the zero byte of the file using the rewind function
rewind(current_file)

# Print out the string
print("Let's print three lines:")

# Assign current_line the value of 1, then print_a_line
current_line = 1
print_a_line(current_line, current_file)

# Increase the count of current_line to 2, then print_a_line
current_line += 1
print_a_line(current_line, current_file)

# Increase the count to 3 then print_a_line
current_line += 1
print_a_line(current_line, current_file)