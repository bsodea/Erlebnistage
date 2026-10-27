import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

for i in range(4):
    t.color("blue")
    t.forward(100)
    t.left(90)

t.penup()
t.forward(100)
t.pendown()

for i in range(3):
    t.color("red")
    t.forward(75)
    t.left(120)

t.penup()
t.backward(175)
t.pendown()

t.color("green")
t.forward(300)

turtle.done()