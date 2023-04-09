from turtle import Turtle
import random


COLORS = ["red", "blue" , "green" , "yellow", "white","pink","orange","light blue", "purple", "light green",]

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.change_color()
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
    
    def move(self):
        """this will make the ball move at the start of the game """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move 
        self.goto(new_x,new_y)
        self.change_color()
    
    def change_color(self):
        self.color(random.choice(COLORS))
    
    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *=0.9
    
    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_speed = 0.1