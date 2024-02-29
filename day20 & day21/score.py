from turtle import Turtle
import os
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        
        script_directory = os.path.dirname(os.path.realpath(__file__))
        data_file_path = os.path.join(script_directory, "data.txt")
        try:
            with open(data_file_path)as data:
                self.high_score =  int(data.read())
        except FileNotFoundError:
            print("High score file not found. Starting with high score of 0.")
        except ValueError:
            print("Error reading high score. Defaulting to 0.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w")as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

# this is if you wanted it to change  
"""
def game_over(self):
self.goto(0, 0)
self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
"""