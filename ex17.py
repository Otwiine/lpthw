# Import argv from sys module 
from sys import argv
# Import exists from os.path module
from os.path import exists

# Unpacks argv
script, from_file, to_file = argv

# Print out string using an f-string
# print(f"Copying from {from_file} to {to_file}")

# open the 'from_file' and assign it to the variable 'in_file'
# read in_file and assign it to the variable 'indata'
in_file = open(from_file);indata = in_file.read()

# Print out the length of 'indata' in bytes using the len() function
print(f"The input file is {len(indata)} bytes long")

# uses exists to check if 'to_file' exists
# print("Ready, hit RETURN to continue, CTRL-C to abort")
input()

# Opens to_file in w mode and assigns it to the variable 'out_file'
out_file = open(to_file, 'w')
# writes 'indata' to the "newly" created "out_file' 
out_file.write(indata)

# print("Alright, all done.")

# closes both the 'out_file' and 'in_file'
out_file.close()
in_file.close()

# Use; semicolon; to; write; multiple; lines; of; code; on; one; line 