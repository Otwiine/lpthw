# Assign the placeholders to the variable
formatter = "{} {} {} {}"

# Uses .format to insert 4 integers into the placeholders
print(formatter.format(1, 2, 3, 4))
# Uses .format to insert 4 strings into the placeholders
print(formatter.format("one", "two", "three", "four"))
# Uses .format to insert 4 Boolean Values inside the placeholders 
print(formatter.format(True, False, False, True))
# Uses .format to insert the formatter variable itself into the placeholders
print(formatter.format(formatter, formatter, formatter, formatter))
# Uses .format to place a multiline string into the placeholders
print(formatter.format(
      "Try your",
      "Own text here",
      "Maybe a poem",
      "Or a song about fear"
))