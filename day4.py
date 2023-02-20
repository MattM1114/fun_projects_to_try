# eg 0 random module , modules are just files that you might want to use
# functions in your main file
# this is how you import a modules
# import
import random

'''


random_int = random.randint(1, 10)
print(random_int)

random_float = random.random()
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")
'''

# ex 0 Heads or Tails
'''


random_side = random.randint(0, 1)

if random_side == 1:
    print("Heads")
else:
    print("Tails")
'''

# eg 1 list
'''
provinces_SA = ["Eastern Cape", "Free State", "Gauteng", "KwaZulu Natal",
                "Limpopo", "Mpumalanga", "North west", "Northern cape", "Western cape"]
list1 = [1, 2, 3, 4]
'''
# this is how you would get a certain part of the list
'''provinces_SA[]'''
# to alter a part of a list is like assigning a variable
'''provinces_SA[1] = "" '''
# add something to the end the list you would append it or
''' provinces_SA.append("")'''
# you another list to this by extending it like this
'''provinces_SA.extend(list1)'''
'''provinces_SA += list1'''
# this is a list of the provinces of south africa
# list normally stuff that is related they also have a set order from 0
# there is more  functions in the documentation

# ex 1 banker roulette with out the choice() function
'''

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num_items = len(names)

random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]

# eg 2 banker roulette with choice()
person_who_will_pay2 = random.choice(names)

print(person_who_will_pay + " is going to buy the meal today!")
print(person_who_will_pay2 + " is going to buy the meal today!")
'''
# ex 2 treasure map this show that you can put a list with in a list
# and show you how you can manipulate that list after .
'''
row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

row = map[vertical - 1]
row[horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
'''
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


computer_choice = random.randint(0, 2)

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors.\n")

if computer_choice == 2 and user_choice == 0:
    print("you win!")
elif computer_choice == 0 and user_choice == 2:
    print("you lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("you win!")
else:
    print("you picked a invalid number, you lose!")
