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

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
choice1 = input(
    "wich way do you wnat to go if left press l if right press r?\n")


if choice1 == "r":
    print("you were attacked by a troll and died.")
    quit
elif choice1 == "l":
    print("Lou come to a lake there is an old bout doked by at the river.")
    choice2 = input(
        "how will you cross the river if you swim press s , if you take the bout press b?\n")
    if choice2 == "b":
        print("You made it across safely and you docked at a castle with three doors.")
        choice3 = input(
            "wich door will you pick if it is the red door press r if it is the yellow door press y if it is the blue door press b?\n")
        if choice3 == "b" or choice3 == "y":
            print("you were killed by an evil wizerd's curse that ate your flesh.")
            quit
        elif choice3 == "r":
            print("you found the treasure and you are now the hier to the kingdom.")
    elif choice2 == "s":
        print("A mermaid has draged you under the water and you drowned and eaten")