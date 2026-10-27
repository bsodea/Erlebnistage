import turtle

screen = turtle.Screen()
t = turtle.Turtle()

screen.register_shape("./bee.gif")

t.shape("./bee.gif")
t.speed(0)
turtle.bgcolor("white")

farben = [
    "#FF6B6B",  # Koralle
    "#FF9F43",  # Orange
    "#FFD166",  # Goldgelb
    "#B8E986",  # Hellgrün
    "#4ECDC4",  # Türkis
    "#45B7D1",  # Himmelblau
    "#5F7ADB",  # Blau
    "#7B61FF",  # Violett
    "#A66CFF",  # Lila
    "#E56BFF",  # Pink-Lila
    "#FF6FAE",  # Rosa
    "#F8C8DC"   # Hellrosa
]

# Diamant aus vielen Dreiecken
for i in range(12):
    t.fillcolor(farben[i])
    t.begin_fill()

    for _ in range(3):
        t.forward(150)
        t.left(120)

    t.end_fill()

    # nächstes Dreieck drehen
    t.left(30)

t.hideturtle()
screen.exitonclick()  # Fenster bei Klick schliessen
turtle.done()
