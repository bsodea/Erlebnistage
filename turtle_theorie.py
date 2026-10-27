import turtle

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(3)
screen = turtle.Screen()

t.color("darkgreen", "lightblue")
t.begin_fill()
for i in range(4):
    t.forward(200)
    t.right(90)
t.end_fill()

screen.exitonclick()
turtle.done()