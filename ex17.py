# Import argv from the sys module
from sys import argv
# Import exists from the os.path module
from os.path import exists

# Unpack the command-line arguments to 3 variables
script, from_file, to_file = argv

# print(f"Copying from {from_file} to {to_file}") (Remove clutter)

# we could do this on one line how? (;)
in_file = open(from_file);indata = in_file.read()
# Opens the 'from_file', stores the object in 'in_file', reads it, and stores it in 'in_data'

# Prints the length (bytes) of the indata file
print(f"The input file is {len(indata)} bytes long")

# Uses exists to check if the file exists returns Boolean Value depending on result
print(f"Does the output file exist? {exists(to_file)}")
# Prompts user to either continue or cancel using CTRL-C
# print("Ready, Hit RETURN to continue, CTRL-C to abort.") (Remove clutter)
# Waits for user choice
input()

# Opens the 'to_file' in write mode, and stores the object in 'out_file'
out_file = open(to_file, 'w')
# Writes in_data to out_file (Basically copying the file)
out_file.write(indata)

print("Alright, all done.")

# Closes both files to free system resources
out_file.close()
in_file.close()