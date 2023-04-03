#Turtle Graphics, Tuples and Importing Modules
# turtle graphics doc https://docs.python.org/3/library/turtle.html
# turtle colors website https://trinket.io/docs/colors
# importing turtle 
import turtle as t
import random
"""form turtle import * """ 
"""form turtle import (the method or variable you want to use )"""
# or 
"""import turtle """
# to install a module 
"""pip install  ( the module you want in the terminal)"""
# https://pypi.org
# this website is a python library with all the modules 
# this will make timmy the turtle , change it's shape and color , 
# then move it well drawing a line a 100 paces forward  then turn right 

timmy = t.Turtle()
timmy.shape("turtle")

"""timmy.forward(100)
timmy.backward(200)
timmy.right(90)
timmy.left(180)
timmy.setheading(0)
timmy.right(90)"""

# ex 0 make timmy draw a square
"""
move = 0

while move < 4:
    timmy.forward(100)
    timmy.right(90)
    move += 1
"""
# or
"""
for _ in range(4):
    timmy.forward(100)
    timmy.right(90)
"""
# ex 1 

#draw 15  dashed lines
"""
for i in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
"""

# ex2
# draw shapes
"""
Color = ["blue", "green" , "yellow", "brown",
        "orange", "maroon", "red", "hot pink"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.fd(50)
        timmy.right(angle)



for shape_side_n in range(3, 11):
    draw_shape(shape_side_n)
    timmy.color(random.choice(Color))

"""
# ex3 random walk

# python_tuple = (1, 2, 3, 4, 5)
# they are ordered
# and they can't be changed or immutable
# to change a tuple you can turn them into a list 
# like this python_list[python_tuple]
""""
t.colormode(255)
direction = [ 0, 90, 180, 270]
timmy.width(15)
timmy.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


for _ in range(300):
    timmy.forward(30)
    timmy.setheading(random.choice(direction))
    timmy.color(random_color())

"""
# ex 4 
"""
t.colormode(255)

timmy.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading()+ size_of_gap)


draw_spirograph(5)
"""







#this will make it exit when I click on the exit button 
screen = t.Screen()
screen.exitonclick()