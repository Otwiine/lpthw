from sys import argv

# Unpacks argv
script, filename = argv

# Open the file and assign it to a variable
txt = open(filename)

# Print out the filename and print out its contents
print(f"Here's your file {filename}:")
print(txt.read())

# Print out instructions and ask for input
print("Type the filename again:")
file_again = input("> ")

# open the file again and assign it to a new variable
txt_again = open(file_again)

# print out the opened file, again
print(txt_again.read())