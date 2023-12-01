import random

#this function will roll the dice
def roll():
    min_value = 1 
    max_value = 6
    roll = random.randint(min_value,max_value)
    
    return roll

# this will check how many players they are 
while True:
    players = input("enter the number of players, (2-4) " )
    if players.isdigit():
        players = int(players)
        if 1 <= players <= 4:
            break
        else:
            print("Invalid amount of players  must between (2-4)")
            print(players)
    else:
        print("must be a digit between 2 and 4 try again")

max_score = 50
players_scores = [0 for i in range(players)]

# this will call the roll faction for each player if the y and will 
while max(players_scores) < max_score:
    
    for player_index in range(players):
        print(f"\nplayer{player_index + 1} turn has started")
        print(f'your total score is {players_scores[player_index]}\n')
        current = 0 
        
        while True:
            should_roll = input("would you like to roll if yes type y ")
            if should_roll.lower() == "y":
                value = roll()
                if value == 1:
                    print("you rolled a 1 your turn is done!")
                    current = 0
                    break
                else:
                    current += value
                    print(f"you rolled a {value}")
                
                print(f"your score is {current}")
                players_scores[player_index] += current
                print(f"your total score is {players_scores[player_index]}")
                
                
            else:
                break

max_score = max(players_scores)
winner = players_scores.index(max_score)
print(f"player{winner+1}is the winner")
