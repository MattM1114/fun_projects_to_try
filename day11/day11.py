
import random
import os
import art

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
#HINT: You can call clear() to clear the output in the console.


def deal_card():
    """this will pick a random card from the list below"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    is_game_over = True
    #Hint 6: Create a function called calculate_score() that takes a List of cards as input 
    #and returns the score. 
    #Look up the sum() function to help you do this.
    def calculate_score(list_cards):
        """This wll calculate the sum of a list of cards"""
        #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
        if sum(list_cards) == 21 and len(list_cards) == 2:
            return 0
        #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
        if 11 in list_cards and sum(list_cards) == 21:
            list_cards.remove(11)
            list_cards.append(1)
        return(sum(list_cards))
    #Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
    def compare(user_score, computer_score):
        you_win = "you win!"
        you_lose = "you lose!"
        if user_score == computer_score:
            return "it is a draw"
        elif computer_score == 0:
            return you_lose
        elif user_score == 0:
            return you_win
        elif user_score > 21:
            return you_lose
        elif computer_score > 21:
            return you_lose
        elif user_score > computer_score:
            return you_win
        else:
            return you_lose


    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    while is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards {user_cards} current score {user_score}")
        print(f"computer first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = False
        else:
            want_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if want_card == "y":
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
                print(f"Your cards {user_cards} current score {user_score}")
                print(f"computer first card: {computer_cards[0]}")
            else:
                is_game_over = False
    #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

    #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

    #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.      


    #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.      
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand: {user_cards} the computer score is : {user_score}")
    print(f"computer cards: {computer_cards} the computer score is :{computer_score}" )
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear_terminal()
    play_game()


