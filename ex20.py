# import argv from the sys module
from sys import argv

# Unpacks command-line arguments into variables
script, input_file = argv

# Define 'print_all' that prints the contents of the file
def print_all(f):
    print(f.read())

# Define 'rewind' function , uses seek(0) to return to start of file
def rewind(f):
    f.seek(0)

# Prints out a line number then the content on that line
def print_a_line(line_count, f):
    print(line_count, f.readline())

# Opens the input file and assigns it to the variable 'current_file'
current_file = open(input_file)

print("First let's print the whole file:\n")

# Prints out contents of the current file
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# Rewinds the current file to the first position, (zero/first byte)
rewind(current_file)

print("let's print three lines:")

# Set current line, print each line of the file with line number 
current_line = 1
print_a_line(current_line, current_file)

# Increase line nuber by 1 
# Set current line, print each line of the file with line number
current_line += 1
print_a_line(current_line, current_file)

# Increase line nuber by 1 
# Set current line, print each line of the file with line number
current_line += 1
print_a_line(current_line, current_file)