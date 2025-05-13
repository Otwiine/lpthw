# import the sys argv from the sys module
from sys import argv

# unpacks argv
script, filename = argv

# Print warning message, gives user chance to cancel using CTRL-C
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you want that, hit RETURN.")

# Wait for user input
input("?")

# Opens the file in write mode and assigns the result to the variable 'target'
print("Opening the file...")
target = open(filename, 'w')

# Truncates the file (not needed since this automatically happens in 'w' mode)
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

# Asks user for 3 lines of input
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# Writes these lines to the file object: target, using .write
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# Close the file to free up system resources
print("And finally, we close it.")
target.close()