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


