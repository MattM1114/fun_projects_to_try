import random

top_of_range = input("type a number please: ")

#this checks if the they typed in a number and changes from a str into int
if top_of_range.isdigit():
    top_of_range = int (top_of_range)
    
    if top_of_range <= 0:
        print('Please make it bigger than 0 next time.')
        quit()
else:
    print('this has to be number please')
    quit()
#this is how to make the program pick a random number
random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input('guess the number: ')
    if user_guess.isdigit():
        user_guess = int (user_guess)
    else:
        print('this has to be number please')
        continue
    
    if user_guess == random_number:
        print('you got it!')
        break
    elif user_guess > random_number:
            print("You were above the number!")
    else:
            print("you are below the number!")

print("you got in", guesses, "guesses")