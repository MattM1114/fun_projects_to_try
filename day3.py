# if ,elif, else, and , not , or
# eg 0 this checks if you are tall enough for a ride based on cm
'''
print("welcome to the rollercoaster ")
height = int(input("What is your height in cm? "))

if height >= 120 :
	print("you are tall enough to go on this ride , congrats.")
else:
	print("sorry you can't go on this ride, your not tall enough.")
'''
# ex 0 this checks if a number is odd or even
'''
num = int(input("Please enter a number "))
if num % 2 == 0 :
	print("even")
else:
	print("odd")
'''
# eg 1 this this will check your height , then check how much you have to pay depending on your age
'''
print("welcome to the rollercoaster ")

height = int(input("What is your height in cm? "))
age = int(input("please enter your age "))

if height >= 120:
	print("you are tall enough to go on this ride , congrats.")
	if age < 12:
		print("You're a child, you have to pay $5  for this ride")
	elif age <= 18:
		print("You're a teen, you have to pay $7  for the ride")
	else:
		print("You're an adult, you have to pay $12  for this ride")
else:
	print("sorry you can't go on this ride, your not tall enough.")
'''
# ex 1 this will check your BMI and tell you if you are within the the right weight for your height in m and kg
'''
weight = input("please enter your weight in kg ")
Height = input("please enter your height in meters ")

BMI = round(float(weight) / float(Height) ** 2)

if BMI < 18:
	print(f"you are underweight, your BMI is {BMI}")
elif BMI <= 25:
	print(f"you have a heathy BMI, your BMI is {BMI}")
else:
	print(f"you are overweight,your BMI is {BMI}")
'''

# ex 2 this will check if it is a leap year or not
'''
year = int(input("Please enter a year "))

if year % 4 == 0:
	if year % 100 == 0:
		if year % 400 == 0:
			print("it is a leap year")
		else:
			print("it is not a leap year")
	else:
		print("it is a leap year")
else:
	print("it is not a leap year")
'''

# eg 2 this will ask if you want a photo taken well on the roller coster
'''
print("welcome to the rollercoaster ")

height = int(input("What is your height in cm? "))
age = int(input("please enter your age "))
bill = 0 

if height >= 120:
	print("you are tall enough to go on this ride , congrats.")
	if age < 12:
		print("child ticket $5")
		bill = 5
	elif age <= 18:
		print("Teen ticket $7")
		bill = 7
	else:
		print("Adult ticket $12")
		bill = 12
	photo = input("Do you want a photo if yes type y if not type n: ")
	if photo == "y":
		bill += 3
	print(f"your final bill is ${bill}")
else:
	print("sorry you can't go on this ride, your not tall enough.")
'''
# ex 3 this will ask what size pizza you want and if you want peperoni or not and if you want extra cheese or not and tells you the bill

'''
print("welcome to python pizza delivery ")

size = input("what size pizza do you want if large type l, if medium type m , if small type s ")
bill = 0
peperoni = input(" if you want peperoni press y if not press n ")
extra_cheese = input(" if you want extra cheese press y if not press n ")


if size == "s":
	bill += 15
	print("small pizza cost $15")
elif size == "m":
	bill += 20
	print("medium pizza cost $20")
elif size == "l":
	bill += 25
	print("large pizza cost $25")

if peperoni == "y":
	if size == "s":
		bill += 2
		print("$2 has been added to your bill")
	else:
		print("$3 has been added to your bill")

if extra_cheese == "y":
	bill += 1
	print("$1 has been added to your bill")

print(f"your total bill is ${bill}")
'''

# logical operators and, or , not
# and both things have to true
# or one thing has to be true
# not reverses a conditions

# ex 4 love score tester
'''
print("Welcome to the love calculator!")
name1 = input("What is your name?\n")
name2 = input("what is your partners name?\n")

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")


true = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")

love = l + o + v + e 

love_score = str(true) + str(love)


if int(love_score) < 10 or int(love_score) > 90:
    print(f"your love is explosive, your love score is {love_score}")
elif int(love_score) >= 40 and int(love_score) <= 50:
    print(f"you are alright together , your score is {love_score}")
else:
    print(f"your love score is {love_score}")
'''

# choose your own adventure game

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input(
    'You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
    choice2 = input(
        'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house")
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You get attacked by an angry trout. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
