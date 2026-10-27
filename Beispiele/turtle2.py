import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

t.color("lightgreen")
t.fillcolor("lightgreen")
t.begin_fill()
t.left(90)
t.circle(75, 180)
t.left(90)
t.forward(150)
t.end_fill()

t.color("darkgreen")
t.fillcolor("darkgreen")
t.begin_fill()
t.forward(175)
t.left(90)
t.circle(120, 180)
t.end_fill()

t.right(90)
t.penup()
t.forward(150)
t.pendown()
t.right(180)
t.color("green")
t.forward(450)

turtle.done()