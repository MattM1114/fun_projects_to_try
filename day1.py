# eg 0 this will print one line

print("hello world!")

# ex 0 this will print multiple lines
'''
print("Day 1 - Python Print Functions")
print("The function is declared like this:")
print("print('what to print')")
'''
# eg 1 this is string manipulation
'''
print("Hello world|\nHello world!\nHello world!")
print("Hello" + " " + "Matthew")
'''
# ex 1 this is after debugging
'''
print("Day 1 - String Manipulation")
print('String Concatenation is done with a "+" sign,')
print('e.g, print("Hello " + "world")')
print("New line is created with a backlash and n")
'''
# eg 2 this is an eg of the input function
'''
input("What is your name? ")
print("Hello" + input("what is your name") )
'''

# Thonny is  a great program to find problems with python code

# ex 2 this is how you find the length of a string that the user input
'''
print(len(input("what is your name ")))
'''
# eg 3 this is an example of variables and how to use them
'''
name = str(input("what is your name "))
print(name)
length_name = len(name)
print(length_name)
'''
# ex 3  this is how to switch the values of to variables
'''
a = input("what is the value of 'a'?")
b = input("What is the value of 'b'?")

c = a
a = b 
b = c

print("a = " + a)
print("b = "+ b)

'''
# rules for naming variables
'''
make sure your code is readable 
you can name them whatever you want as long as they don't start with a number
They can't have a space in between if you are using two words so instead you would use _ eg "user_name" 
you cant use privileged words like the name of  that are built functions in  
'''

# band name generator
# this is a simple program that takes the name of the user's birth city or town and their 1st pet name or the type of pet and joins them eg Durban Honey
"""
print("Hey future band leader or rapper let's find you a name")

birth_place = input("What is the name of the city or town you were born in?\n")
pet = input("What was your first pet or what was it's name?\n")

print("Your band or rapper name could be " + birth_place + ' ' + pet + '.')
"""
