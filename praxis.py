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

# TODO: Farbe setzen
t.begin_fill()
t.goto(0, 100)
# TODO: Dreieck machen
t.end_fill()

screen.exitonclick()
turtle.done()
