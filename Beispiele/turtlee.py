import turtle
from util import draw_grid, save_image

t = turtle.Turtle()

t.shape("turtle")
t.speed(10)

# Head
t.teleport(0, 0)
t.color("light green")
t.begin_fill()

t.circle(40)

t.end_fill()

# Eye

t.teleport(-15, 50)
t.color("black")
t.begin_fill()

t.circle(3)

t.end_fill()

# Feet

t.teleport(0, 0)
t.color("light green")
t.begin_fill()

t.setheading(0)
t.forward(50)
t.setheading(270)
t.forward(20)
t.setheading(180)
t.forward(50)
t.setheading(90)
t.forward(20)

t.end_fill()

t.teleport(150, 0)

t.begin_fill()
t.setheading(0)
t.forward(50)
t.setheading(270)
t.forward(20)
t.setheading(180)
t.forward(50)
t.setheading(90)
t.forward(20)

t.setheading(0)

t.end_fill()

# Tail

t.color("light green")
t.teleport(190, 40)

t.begin_fill()

t.setheading(320)
t.forward(30)
t.setheading(180)
t.forward(10)
t.setheading(320)
t.backward(30)
t.setheading(0)

t.end_fill()

# Shell
t.teleport(0, 0)
t.color("green")
t.begin_fill()

t.forward(200)
t.setheading(90)
t.circle(100, 180)

t.end_fill()

draw_grid(interval=10)
save_image(20)
