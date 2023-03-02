
# today's import for the final project
import art


# simple function

'''
def greet():
    print("Hello world")
    print("How do you do ?")
    print("Isn't the weather nice today?")


greet()
'''

# Function that allows for input
'''

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")


greet_with_name("Matthew")

'''
# parameter is the name of the data being pass though argument is the actual value of the parameter

# Function with more than 1 input

'''
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
'''

'''
greet_with("Matthew", "south Africa")
'''
# a positional arguments are when you an argument is assigned to a parameter based on them position being the same that is what
# has been done above

# keyword arguments are not based on position but rather they are based on how you assign them kind of  like variables
# look below for an example
'''
greet_with(location="south africa", name="Matthew")
'''

# ex1

# Write your code below this line 👇
'''

def paint_calc(height, width, cover):
    num_of_cans = round((height * width)/cover)
    print(f"You'll need {num_of_cans} cans of paint.")
'''

# Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.
# 🚨 Don't change the code below 👇
'''
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
'''

# ex 2
# Write your code below this line 👇

'''
def prime_checker(number):
    is_prime = True
    for i in range(2, number - 1):
        if number % i == 0:
            is_prime = False
    if is_prime == False:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")
'''

# Write your code above this line 👆
# Do NOT change any of the code below👇
'''
n = int(input("Check this number: "))
prime_checker(number=n)
'''
# final project
# Caesar cipher
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# this function will encrypt the message
''' 
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")
'''
# this function will decrypt the message
'''

def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"The decoded text is {plain_text}")
'''
# this ask if you want to encrypt the message or decrypt the message
'''
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == 'decode':
    decrypt(cipher_text=text, shift_amount=shift)
'''

# this is all of that combined into one function


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}")


should_end = False
while not should_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
# TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
# Try running the program and entering a shift number of 45.
# Add some code so that the program continues to work even if the user enters a shift number greater than 26.
# Hint: Think about how you can use the modulus (%).
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
