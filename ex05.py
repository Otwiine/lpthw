name = 'Zed A. Shaw'
age = 35 # Not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

height_cm = round(height * 2.54) # Round to 2 dcm
weight_kgs = round(weight /  2.205) # Round to 2 dcm

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall, that's about {height_cm} cm tall.")
print(f"He's {weight} pounds heavy, that's about {weight_kgs} kgs heavy.")
print("Acyually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# 1 inch = 2.54 cm (x * 2.54)
# 1 pound = 0.453592 kg (x / 2.205)