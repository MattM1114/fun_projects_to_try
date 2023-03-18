import turtle

# get name from user
name = input("Enter a name: ")

# set up turtle
t = turtle.Turtle()
t.speed(0)

# draw cake base
t.penup()
t.goto(0, -100)
t.pendown()
t.begin_fill()
t.color("orange")
t.circle(100)
t.end_fill()

# draw cake icing
t.penup()
t.goto(0, -50)
t.pendown()
t.begin_fill()
t.color("pink")
t.circle(50)
t.end_fill()

# draw candles
for i in range(8):
    t.penup()
    t.goto(-50 + i * 14, 20)
    t.pendown()
    t.color("bl")
    t.begin_fill()
    t.forward(10)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(10)
    t.end_fill()

# write message
t.penup()
t.goto(0, 100)
t.color("black")
t.write("Happy Birthday, {}!".format(name), align="center", font=("Arial", 24, "bold"))

turtle.done()
