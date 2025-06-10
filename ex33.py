i = 0
numbers = []

while i < 6:
    print(f"At the top is i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)

# STUDY DRILLS

def while_loop(inc):
    i = 0
    x = 10
    numbers = []

    while i < x:
        print(f"At the top is i is {i}")
        numbers.append(i)

        i = i + 1 + inc
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)

while_loop(3)
