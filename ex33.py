# i = 0
# numbers = []

# while i < 6:
#     print(f"At the top i is {i}")
#     numbers.append(i)

#     i = i + 1
#     print("Numbers now: ", numbers)
#     print(f"At the bottom i is {i}")


# print("The numbers: ")

# for num in numbers:
#     print(num)


def iterate(iteration, inc):
    # i = 0
    numbers = []

    for i  in range(0, iteration, inc):
        print(f"At the top i is {i}")
        numbers.append(i)

        # i = i + inc
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)

iterate(100, 20)