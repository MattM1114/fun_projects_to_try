# more turtle graphics, Event Listeners,State and multiple instances

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.fd(10)

def turn_left():
    tim.left(10)
# or 
"""
def turn_left():
    new_head = tim.heading() + 10
    tim.setheading(new_head)
"""


def turn_right():
    tim.right(10)
# or 
"""
def turn_right():
    new_head = tim.heading() - 10
    tim.setheading(new_head)
"""


def move_backward():
    tim.backward(10)

def clear_screen():
    tim.reset()

# or 
'''
def clear_screen():
    tim.clear()
    tim.home()
    tim.clear()
'''

# to pass a function into another
# you can use as an argument but without the ()
# functions that take other function as arguments are called 
# high order functions


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()