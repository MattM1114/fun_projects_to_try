# Welcome to my Python class!

# Variables
name = "Alice"
age = 25
is_student = True
fruits = ["apple", "banana", "cherry"]
person = {"name": "Bob", "age": 30}

# Functions
def greet(name):
    print("Hello, " + name + "!")

def calculate_sum(a, b):
    return a + b

# Loops
print("Printing fruits using for loop:")
for fruit in fruits:
    print(fruit)

i = 0
print("Printing numbers using while loop:")
while i < 5:
    print(i)
    i += 1

# Comments
"""
This is a multiline comment.
It can be used to document the code.
"""

# Program
print("Welcome to my program!")
greet(name)
total = calculate_sum(age, len(fruits))
print("The total is:", total)

print("Printing person information:")
for key, value in person.items():
    print(key + ":", value)
