from turtle import Turtle
import random

COLORS = ["white", "blue" , "green", "red"]
class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.change_color()
        self.speed("fastest")
        self.refresh()
    def change_color(self):
        self.color(random.choice(COLORS))
    def refresh(self):
        self.change_color()
        random_x = random.randint(-270, 280)
        random_y = random.randint(-270, 280)
        self.goto(random_x, random_y)
