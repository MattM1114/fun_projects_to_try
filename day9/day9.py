# dict = dictionary
'''programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
"Function": "A piece of code that you can easily call over and over again."}'''

'''print(programming_dictionary["Bug"])'''
# this is how a dict looks like and how to retrieve item to a dict
'''programming_dictionary["loop"] = "The action of doing something over and over again."
print(programming_dictionary)'''
# this is how you would add to a dict
'''empty_dict = {}'''
# this is an empty dict
''' programming_dictionary = {}'''
# this how to wipe a dict

'''programming_dictionary["Bug"] = "A moth  in your computer."
print(programming_dictionary)'''
# this is how to edit a dict
'''for key in programming_dictionary:
    print(key)'''
#this is how to loop though the key of dict
'''    print(programming_dictionary[key])'''
#this is how to loop  though the values in the loop
# ex1
'''
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"


# 🚨 Don't change the code below 👇
print(student_grades)
'''

# nesting


# Nesting a list in a Dict and a dict in a list 
'''
travel_log = [
{"country":"France", "cities_visited": ["paris"," Dijon"] },
{"country":"England", "cities_visited": ["london", "manchester", ],"total_visits": 3} ]
'''
# ex 2
'''
travel_log = [
{
"country": "France",
"visits": 12,
"cities": ["Paris", "Lille", "Dijon"]
},
{
"country": "Germany",
"visits": 5,
"cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(name, visit_count, cities_visited):
    new_country = {}
    new_country["country"] = name
    new_country["visits"] = visit_count
    new_country["cities"] = cities_visited
    travel_log.append(new_country)    



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
'''

import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
#HINT: You can call clear() to clear the output in the console.
import art
print(art.logo)


playing = True
while playing :
    bidders = []


    def bidders_update():
        new_bid = {}
        name = input("what is your name?: ")
        bid = int(input("What is your bid: $"))
        new_bid.update({name:bid})
        bidders.append(new_bid)
    

    bidders_update()
    more_bid = input("Are there any other bidders? Type 'yes or 'no'. ").lower()

    if more_bid == "yes":
        clear_terminal()
        bidders_update()