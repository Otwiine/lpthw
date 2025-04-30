from sys import argv

script, user_name, alt_name = argv 
prompt = '>> '

print(f"Hi {user_name} {alt_name}, I'm the {script} script.")
print
print("I'd like to ask you a few questions,")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"How old are you {user_name}?")
age = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright {user_name} {alt_name}, so you said {likes} about liking me.
You're {age} years old.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")