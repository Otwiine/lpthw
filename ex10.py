# Use \t to cteate a tab (4 spaces)
tabby_cat = "\tI'm tabbed in."
# Use \n to start new line
persian_cat = "I'm split\non a line."
# Use \\ to create a single backslash
backslash_cat = "I'm \\ a \\ cat."

# Create a tabbed in list 
fat_cat = ''' 
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

# Print out the variables
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# Utilizes escape sequences
thin_cat = "\t\\This is\n\t\\X\bthe \"thin cat\"\n"
# the (r" ") prints out the raw string, ignoring the escape sequences
raw_thin_cat = r"\t\\This is\n\t\\X\bthe \"thin cat\"\n"

print(thin_cat)
print(raw_thin_cat)

# Testing more Escape Sequences
print("Hello\fWorld\n")  # NEEDS BETTER EXPLANATION
print("Hello\vWorld\n")  # \v (Vertical Tab)
print("Hello\rWorld\n")  # NEEDS BETTER EXPLANATION
print("\U0001F600\n")  # \Uxxxxxxxx (32-bit Unicode)
print("\101\n")  # \000 (Octal Character)
print("\x41\n")  # \xhh (Hexadecimal Character)
print("\u2764\n")  # \uxxxx (16-bit Unicode)