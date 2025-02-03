from sys import argv

# 'Unpacks' argv
script, filename = argv

print(f"Were going to erase {filename}.")
print("If you don't want that hit CTRL-C (^C)")
print("If you do want that, hit RETURN.")

# Placeholder/Promt for user to either break or continue
input("?")

# Open the file in write mode
print("Opening the file...")
target = open(filename, 'w')

# Not needed because 'w' mode truncates the file
# print("Truncating the file. Goodbye!")
# target.truncate()

print("Now i'm going to ask you for three lines.")

# Prompt the user for input to assign to the variables
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# Write the new lines to the file, using newline characters to skip lines
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# Close the file using .close()
print("And finally, we close it.")
target.close()