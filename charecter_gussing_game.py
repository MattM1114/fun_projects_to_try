
# this game is about guessing if a person is a character or not  

answer = 0
# the user will be asked these questions
person = []
name = str(input('what is your name ? '))
age = int(input('what is your age ? '))
color = str(input('what is your favorite color ? '))
food = input('what is your favorite food ? ')
job = input('what is your dream job ? ')

person.append(name, age, color, food, job)
# the tester will be ask these questions.
name_1 = str(input())
age_1 = int(input())
color_1 =input
#this loop will de
while answer < 5:
    if name == name_1:
        print("you have the same name as " + name_1)
        answer = answer + 1
    else:
        print("your names are  different form " + name_1)

    if age == c:
        print("you are the same age as " + name_1)
        answer = answer + 1
    else:
            print("you and "+ name_1 +" are different ages.")

    if color == color_1:
            print("you have the same favorite color")
            answer = answer + 1
    else:
            print("you and "+ name_1 + " have different favorite colors")

    if food == food_1:
        print("you like the same food as " + name_1)
        answer = answer  + 1 
    else:
        print("you don't like the same food")

    if job == job_1:
        print("you and {name_1} have the same dream job")
        answer = answer + 1
    else:
        print("you have different dream jobs")
        quit

def are_you_the_character():
    if answer  == 5:
        print("you are the character {name_1}.")
    else:
        print("you are not character {name_1}.")

print(are_you_the_character)

\\\ this is a doc \\\