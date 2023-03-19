############DEBUGGING#####################

# Describe Problem
'''
def my_function():
    """before i would never reach 20"""
    for i in range(1, 21):
        if i == 20:
            print("You got it")

my_function()
'''

# Reproduce the Bug
'''
""" the error occurred when dice_num was == 6 because six is out range"""
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])
'''
# Play Computer
'''
"""this did not have an option for the year 1994 """
year = int(input("What's your year of birth? "))
if year > 1980 and year <= 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")
'''
# Fix the Errors
''''
"""the error was that the print line was not  and the string was not a functional one indented and that age is a str instead of an int"""
age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")
'''
#Print is Your Friend
"""the varibels were not re assigned porperly to the users inputs"""
'''
pages = 0
word_per_page = 0
pages += int(input("Number of pages: "))
word_per_page += int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
'''


#Use a Debugger
'''
def mutate(a_list):
    """this code was not adding the new to the list but when using a debugger you can see
    that b_list.append(new_item) was not indented correctly"""
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])
'''
# ex 1
'''
number = int(input("Which number do you want to check?"))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
'''
#ex 2
'''
year = int(input("Which year do you want to check?"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
'''
# ex 3 
'''
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
'''