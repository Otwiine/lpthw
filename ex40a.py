# DICT
# mystuff = {'apple': "I AM APPLES!"}
# print(mystuff['apple'])

# MODULE
import mystuff # (from mystuff import apple)

mystuff.apple()
print(mystuff.tangerine)

# COMPARE
# mystuff['apple'] # get apple from a dict
# mystuff.apple() # get apple from the module
# mystuff.tangerine # same thing, it's just a variable

# CLASS AND OBJECT*
class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM APPLES!")

thing = MyStuff()
thing.apple()
print(thing.tangerine)

# 3 WAYS TO GET 'THINGS FROM THINGS'

# dict style
# mystuff['apples'] 

# module style
# mystuff.apple()
# print(mystuff.tangerine)

# class style
# thing = MyStuff()
# thing.apple()
# print(thing.tangerine)