test = 30 == 30

if test is not True:
    print(False)

else:
    print(True)


# not - Reverses a condition (not True == False)  (not False == True)
# or - Returns True if at least one condition is True, False if both conditions are False 
# and - Returns True only if both conditions are True, returns false if any condition is False
# not or - Reverses an 'or' condition
# not and - Reverses an 'and' condition
# != - not equal to
# == - equal checks wether 2 conditions are equal to eachother

# When solving 'not' has higher rank than 'and', and 'and' has higher precedence than 'or'


# Simple password
password = input("Password: ")
while password != "ojo1605":
    print("Access Denied!")
    password = input("Password: ")

print("Access Granted")