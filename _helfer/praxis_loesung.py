import turtle

t = turtle.Turtle()
t.shape("turtle")
screen = turtle.Screen()

# Quadrat
t.fillcolor("beige")
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()

t.fillcolor("red")
t.begin_fill()
t.goto(0, 100)
t.forward(100)
t.left(135)
t.forward(70.7)
t.left(90)
t.forward(70.7)
t.end_fill()

screen.exitonclick()
turtle.done()
