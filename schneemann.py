import turtle

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
screen = turtle.Screen()
screen.bgcolor("black")

# Unterer Schneeball
t.penup()
t.goto(0, -150)
t.pendown()
t.color("white", "white")
t.begin_fill()
t.circle(60)
t.end_fill()

# Mittlerer Schneeball
t.penup()
t.goto(0, -50)
t.pendown()
t.begin_fill()
t.circle(40)
t.end_fill()

# Kopf
t.penup()
t.goto(0, 20)
t.pendown()
t.begin_fill()
t.circle(30)
t.end_fill()

# Augen zeichnen
t.penup()
t.goto(-10, 60)
t.pendown()
t.dot(6, "black")

t.penup()
t.goto(10, 60)
t.pendown()
t.dot(6, "black")

# Nase zeichnen
t.penup()
t.goto(-7.5, 40)
t.setheading(0)
t.color("orange")
t.pendown()
t.begin_fill()
for i in range(3):
    t.forward(15)
    t.left(120)
t.end_fill()

# Hut zeichnen
t.penup()
t.goto(-25, 75)
t.setheading(0)
t.color("brown")
t.pendown()
t.begin_fill()
for i in range(2):
    t.forward(50)
    t.left(90)
    t.forward(10)
    t.left(90)
t.end_fill()

t.penup()
t.goto(-15, 85)
t.pendown()
t.begin_fill()
for i in range(2):
    t.forward(30)
    t.left(90)
    t.forward(25)
    t.left(90)
t.end_fill()

screen.exitonclick()
turtle.done()
