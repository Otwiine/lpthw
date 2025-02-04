name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# Converts inches into centimetres
cm = height * 2.54
# Converts pounds into kilograms
kgs = weight * 0.453592

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}")

# Repeats code but uses Metric system

print(f"\nLet's talk about {name}.")
# Uses round() function to make reading clearer
print(f"He's {round(cm)} cm tall.")
print(f"He's {round(kgs)} kgs heavy.")
print("Actually that's not that heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + cm + kgs
print(f"If I add {age}, {round(cm)}, and {round(kgs)} I get {round(total)}")