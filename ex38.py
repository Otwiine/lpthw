ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

# While there are less than 10 items in the stuff, pop the last item from more_stuff and append it to stuff.
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go", stuff)

print("Let's do some things with stuff")

# Print the second item in the list
print(stuff[1])
#Print the last item in the list
print(stuff[-1]) # woah! fancy
# Pop the last item off the list
print(stuff.pop())
# Joins the elements of the list with a ' ' seperator
print(' '.join(stuff)) # what? cool!
# Slices the list and joins the elements at that index with a #
print('#'.join(stuff[3:5])) # super stellar!