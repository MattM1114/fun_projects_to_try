# This is a single-line comment

"""
This is a
multi-line
comment
"""

name = "Alice"   # A string variable
age = 25         # An integer variable
price = 2.99     # A float variable
is_student = True  # A boolean variable

my_list = [1, 2, 3, 4]    # A list variable
my_tuple = ("apple", "banana", "cherry")   # A tuple variable
my_set = {"apple", "banana", "cherry"}     # A set variable


def add_numbers(x, y):
    sum = x + y
    return sum

result = add_numbers(3, 5)
print(result)  # Output: 8

"""
while condition:
    # Code to execute while condition is true
"""

count = 1
while count <= 5:
    print(count)
    count += 1

""""
for item in sequence:
    # Code to execute for each item in sequence
"""

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

