import turtle

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
screen = turtle.Screen()

t.color("yellow", "yellow")
t.begin_fill()
for i in range(5):
    t.forward(200)
    t.right(144)
t.end_fill()

screen.exitonclick()
turtle.done()
