# Import argv from the sys module
from sys import argv

# Unpacks argv into two variables
script, filename = argv

# Opens the file passed in from the cmd line and stores it in the file object 'txt'
txt = open(filename)

# Prints out the filename
print(f"Here's your file {filename}:")
# Reads the contents of the file and prints them to the screen
print(txt.read())
# Close txt file
txt.close()

# Prompts user to type filename again
print("Type the filename again:")
# Stores user input in 'file_again'
file_again = input("> ")

# Opens the file passed into file_again and stores it in the file object 'txt_again'
txt_again = open(file_again)

# Reads the contents of txt_again and prints them
print(txt_again.read())

# Close file
txt_again.close()