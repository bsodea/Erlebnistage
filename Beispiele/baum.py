import turtle

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
screen = turtle.Screen()

# Baumstamm zeichnen
t.color("brown", "brown")
t.begin_fill()

for i in range(2):
    t.forward(40)
    t.left(90)
    t.forward(100)
    t.left(90)

t.end_fill()

# Zur Baumkrone gehen
t.penup()
t.goto(20, 90)
t.pendown()

# Baumkrone zeichnen
t.color("green", "green")
t.begin_fill()
t.circle(50)
t.end_fill()

screen.exitonclick()
turtle.done()
