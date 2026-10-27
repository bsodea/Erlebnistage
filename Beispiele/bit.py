import turtle

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
screen = turtle.Screen()

# Gebäude
t.color("gray")
t.begin_fill()

for i in range(2):
    t.forward(300)
    t.left(90)
    t.forward(250)
    t.left(90)

t.end_fill()

# Fenster
def fenster(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("lightblue")
    t.begin_fill()

    for i in range(4):
        t.forward(40)
        t.left(90)

    t.end_fill()

# Fenster zeichnen
fenster(28, 182)
fenster(96, 182)
fenster(164, 182)
fenster(232, 182)

fenster(28, 114)
fenster(96, 114)
fenster(164, 114)
fenster(232, 114)

# Tür
t.penup()
t.goto(130, 0)
t.pendown()
t.color("brown")
t.begin_fill()

for i in range(2):
    t.forward(40)
    t.left(90)
    t.forward(70)
    t.left(90)

t.end_fill()

screen.exitonclick()
turtle.done()