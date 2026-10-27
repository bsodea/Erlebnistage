import turtle

t = turtle.Turtle()
screen = turtle.Screen()

t.color("red")
t.setheading(0)
t.forward(200)

t.color("orange")
t.setheading(90)
t.forward(200)

t.color("yellow")
t.setheading(180)
t.forward(200)

t.color("green")
t.setheading(270)
t.forward(200)

screen.exitonclick()
turtle.done()
