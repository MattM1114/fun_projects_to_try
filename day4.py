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


names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num_items = len(names)

random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]

# eg 2 banker roulette with choice()
person_who_will_pay2 = random.choice(names)

print(person_who_will_pay + " is going to buy the meal today!")
print(person_who_will_pay2 + " is going to buy the meal today!")
