# Step 1

from .hangman_words import word_list
from .hangman_art import stages, logo
import random

{
    "python.autoComplete.extraPaths": ["FUN_PROJECTS_TO_TRY/day7"]
}


print(logo)

# this is how to get the word from the list randomly
word = random.choice(word_list)
# this will find the length of the and will display a _ in place of the letter


display = []
word_length = len(word)
for _ in range(word_length):
    display += "_"

# this  while loop won't end until you get everything correct or until the man dies
end_of_game = False
lives = 6

while not end_of_game:
    guess = input("guess a letter ").lower()

    # this will show put the letter you guess in the list in replacement for _ in the list for each word you get correct

    for position in range(word_length):
        letter = word[position]
        if letter == guess:
            display[position] = letter
    if guess not in word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("you lose.")

    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("you win")

    print(stages[lives])