import random
# eg 0 loops
# For Loop with Lists
"""
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)
"""

# ex 0 average height of students
# This will calculate the average height of a number of people using for loops and lists.
# I was not allowed to use the len() and sum() functions because it would not help me learn about for loops and would be to easy.
'''
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])


total_height = 0
number_of_students = 0

for height in student_heights:
    total_height += height

for students in student_heights:
    number_of_students += 1

average = round(total_height/number_of_students)
print(average)
'''

# ex 1 best score
# this program use a forloop to figure out the best score for a number of student like the max() function would
'''
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score


print(f"The highest score in the class is: {max_score}")
'''
# eg 1 range()
# this program figures out the total of all the numbers from 1 - 100 which is 5050
'''
total = 0
for number in range(1, 101):
    total += number
print(total)
'''
# ex 2 this program figures out the total of even numbers from 1 - 100 which is 2550
''' 
total = 0
for number in range(0, 101, 2):
    total += number
print(total)
'''
# if you want total of the odd numbers from 1 - 100 which is 2500 then you would do this:
'''
total = 0
for number in range(1, 101, 2):
    total += number
print(total)
'''
# ex 3 fizzbuzz
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

# ex 4 Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level - Order not randomized:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
'''
password = ""

for char in range(1, nr_letters + 1): 
    password += random.choice(letters)

for sym in range(1, nr_symbols + 1):
    password += random.choice(symbols)

for num in range(1, nr_numbers + 1): 
    password += random.choice(numbers)


print(password)
'''
# Hard Level - Order of characters randomized:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for sym in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

for num in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
password = "".join(password_list)
print(password)
