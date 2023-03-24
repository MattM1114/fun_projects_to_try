import turtle

# get name from user
name = input("Enter a name: ")

# set up turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# define function for drawing a flame
def draw_flame(size):
    t.color("yellow", "red")
    t.begin_fill()
    t.right(45)
    t.forward(size)
    t.right(90)
    t.forward(size)
    t.right(90)
    t.forward(size)
    t.right(90)
    t.forward(size)
    t.right(135)
    t.forward(size * 0.8)
    t.end_fill()

# draw cake base
t.penup()
t.goto(0, -150)
t.pendown()
t.begin_fill()
t.color("#FFBF00")
t.circle(150)
t.end_fill()

# draw cake icing
t.penup()
t.goto(0, -120)
t.pendown()
t.begin_fill()
t.color("#FFE5B4")
t.circle(120)
t.end_fill()

# draw candles and flames
t.color("#FFD700")
for i in range(8):
    t.penup()
    t.goto(-50 + i * 20, 70)
    t.pendown()
    t.begin_fill()
    t.forward(10)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(10)
    t.end_fill()
    t.penup()
    t.goto(-45 + i * 20, 100)
    t.pendown()
    draw_flame(8)

# draw message
t.penup()
t.goto(0, 220)
t.color("#A91E1E")
t.write("Happy Birthday, {}!".format(name), align="center", font=("Arial", 36, "bold"))

# add custom message
t.penup()
t.goto(0, -50)
t.color("#A91E1E")
t.write("You're amazing!", align="center", font=("Arial", 24, "bold"))

# print birthday wish and compliment
print("Happy birthday, {}! I hope your day is filled with joy and happiness. You're an amazing person and you deserve the best!".format(name))

turtle.done()

