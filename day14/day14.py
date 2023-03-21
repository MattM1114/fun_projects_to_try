import os

# format the account data into printable format
def account_data(account):
    '''format the account data into printable format'''
    account_name = account["name"]

    account_descr = account["description"]

    account_country = account["country"]

    return(f"{account_name} a {account_descr} from {account_country}")

## use if statement to check if user is correct.
def check_answer(Guess, a_followers, b_followers):
    """take the user, and the accounts ,and check if the user is correct"""
    if a_followers > b_followers:
        return Guess == "a"
    else:
        return Guess == "b"




def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
#HINT: You can call clear() to clear the output in the console.

# logo art
import art
print(art.logo)
playing = True 
#score keeping
score = 0

# genrate a random account from data
from game_data import data
import random

account_b = random.choice(data)
# make the game repeatable
while playing:
    account_a = account_b

    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"compare a: {account_data(account_a)}")

    print(art.vs)

    print(f"against b: {account_data(account_b)}")
    # ask user for a guess 
    guess = input("who has more follwers 'a' or 'b'").lower()

    # check if user is correct
    ## Get follwer count of each account.
    a_follower_count = account_a['follower_count']
    b_follwer_count = account_b['follower_count']

    is_correct = check_answer(guess, a_follower_count, b_follwer_count)

    # clear the screen
    clear()
    print(art.logo)


    # give feedback
    if is_correct:
        score += 1
        print(f"you are right!your score is {score}")

    else:
        print(f"sorry you were wrong. Final score {score}")
        playing = False

