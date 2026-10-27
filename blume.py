import turtle

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
screen = turtle.Screen()

# Stängel zeichnen
t.penup()
t.goto(0, 0)
t.setheading(270)
t.pendown()
t.color("green")
t.pensize(5)
t.forward(150)
t.penup()
t.goto(0, 0)
t.pendown()

# Blütenblätter zeichnen
t.color("red", "red")
t.begin_fill()
for i in range(6):
    for j in range(2):
        t.circle(50, 60)
        t.left(120)
    t.left(60)
t.end_fill()

screen.exitonclick()
turtle.done()
