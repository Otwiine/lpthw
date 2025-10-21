# numbers = []

# def iterate(iteration, inc):
#     i = 0
#     while i < iteration:
#         print(f"At the top i is {i}")
#         numbers.append(i)

#         i = i + inc
#         print("Numbers now: ", numbers)
#         print(f"At the bottom i is {i}")

# iterate(12, 2)

# print("The numbers: ")

# for num in numbers:
#     print(num)

# STUDY DRILL

numbers = []

def iterate(iteration):

    for i in range(0, iteration) :
        print(f"At the top i is {i}")
        numbers.append(i)

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

iterate(12)

print("The numbers: ")

for num in numbers:
    print(num)