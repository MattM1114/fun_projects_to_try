import random

#this will count the points you and the pc have 
user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
#this will get the users answer and quit if they pick q
    user_input = input('Type Rock/Paper/Scissors or Q to quit: ').lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked:", computer_pick + ".")
# here we will check who won  
    if user_input == 'rock' and computer_pick == 'scissors':
        print("you won!")
        user_wins += 1
        continue
    elif user_input == 'paper' and computer_pick == 'rock':
        print("you won!")
        user_wins += 1
        continue
    elif user_input == 'scissors' and computer_pick == 'paper':
        print("you won!")
        user_wins += 1
        continue
    elif user_input == 'paper' and computer_pick == 'paper':
        print("this was a  tie you and the computer both win")
        user_wins += 1
        computer_wins +=1
        continue
    elif user_input == 'rock' and computer_pick == 'rock':
        print("this was a  tie you and the computer both win")
        user_wins += 1
        computer_wins +=1
        continue
    elif user_input == 'scissors' and computer_pick == 'scissors':
        print("this was a  tie you and the computer both win")
        user_wins += 1
        computer_wins +=1
        continue
    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("the computer won", computer_wins,"times.")
print("Goodbye")