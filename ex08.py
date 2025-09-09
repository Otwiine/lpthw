# Assigns .format placeholders to the 'formatter variable
formatter = "{} {} {} {}"

# Inserts Integers into the placeholders using .format
print(formatter.format(1, 2, 3, 4))
# Inserts strings into the placeholders
print(formatter.format("one", "two", "three", "four"))
# Inserts boolean values into the placeholders
print(formatter.format(True, False, False, True))
# Inserts the formatter var into into the placeholder
print(formatter.format(formatter, formatter, formatter, formatter))
# Inserts four seperate strings into the placeholders
print(formatter.format(
    "Its OJO",
    "How you doing?",
    "Everything alright?",
    "I would hope so"
))