# Imports argv from the sys module
from sys import argv

# Unpacks argv (Unpacks command line arguments)
script, filename = argv

# Opens the {filename} file and assigns the (file object) to the txt variable
txt = open(filename)

# Prints the filname
print(f"Here's your file {filename}:")
# uses .read to "read" the file, prints the file
print(txt.read())

# Close the file after reading
txt.close()

# Prompts user to type filename again
print("Type the filename again:")
# Asks user for input, and will assign it to the file_again variable
file_again = input("> ")

# opens the file
txt_again = open(file_again)

# Reads and prints the file (again)
print(txt_again.read())

# Close the file again
txt_again.close()