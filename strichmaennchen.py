import turtle

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pencolor("white")
t.pensize(3)
screen = turtle.Screen()
screen.bgcolor("black")

# Kopf
t.penup()
t.goto(0, 50)
t.pendown()
t.circle(20)

# Körper
t.penup()
t.goto(0, 50)
t.pendown()
t.goto(0, -30)

# Arme
t.penup()
t.goto(-40, 10)
t.pendown()
t.goto(0, 30)
t.goto(40, 10)

# Beine
t.penup()
t.goto(0, -30)
t.pendown()
t.goto(-30, -70)
t.penup()
t.goto(0, -30)
t.pendown()
t.goto(30, -70)

screen.exitonclick()
turtle.done()

 