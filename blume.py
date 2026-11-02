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

# Blüte
t.color("red")
for i in range(4):
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.left(90)

screen.exitonclick()
turtle.done()
