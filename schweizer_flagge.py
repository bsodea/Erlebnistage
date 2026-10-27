import turtle

t = turtle.Turtle()
t.speed(5)
t.hideturtle()
screen = turtle.Screen()

# Roter Hintergrund
t.penup()
t.goto(-100, 100)
t.pendown()
t.color("red", "red")
t.begin_fill()

for i in range(4):
    t.forward(200)
    t.right(90)

t.end_fill()

# Weisses Kreuz – senkrechter Balken
t.penup()
t.goto(-20, 60)
t.pendown()
t.color("white", "white")
t.begin_fill()

for i in range(4):
    t.forward(40)
    t.right(90)
    t.forward(120)
    t.right(90)

t.end_fill()

# Weisses Kreuz – waagrechter Balken
t.penup()
t.goto(-60, 20)
t.pendown()
t.begin_fill()

for i in range(2):
    t.forward(120)
    t.right(90)
    t.forward(40)
    t.right(90)

t.end_fill()

screen.exitonclick()
turtle.done()