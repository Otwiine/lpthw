# Import argv from the sys module
from sys import argv

# Unpacks the command line arguments (into separate variables)
script, filename = argv

# Opens the file and assigns it to 'target'
target = open(filename)

# Reads the file and prints it's contents
print(f"Here is what is in {filename}\n")
print(target.read())

# Close the file to free system resources
target.close()