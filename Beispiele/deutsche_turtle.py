

import turtle as _turtle

# ==========================================
# Deutsche Turtle-Wrapper
# ==========================================

# Bewegung
vor = _turtle.forward
zurueck = _turtle.backward
links = _turtle.left
rechts = _turtle.right
gehe_zu = _turtle.goto
setze_x = _turtle.setx
setze_y = _turtle.sety
gehe_zum_start = _turtle.home
position = _turtle.position
richtung = _turtle.heading

# Stift
stift_hoch = _turtle.penup
stift_runter = _turtle.pendown
stiftfarbe = _turtle.pencolor
stiftgroesse = _turtle.pensize
stift = _turtle.pen
stift_zuruecksetzen = _turtle.reset
loeschen = _turtle.clear

# Zeichnen
kreis = _turtle.circle
punkt = _turtle.dot
bogen = _turtle.circle
fuellen_beginnen = _turtle.begin_fill
fuellen_beenden = _turtle.end_fill
fuellfarbe = _turtle.fillcolor
farbe = _turtle.color

# Turtle-Einstellungen
geschwindigkeit = _turtle.speed
verstecken = _turtle.hideturtle
anzeigen = _turtle.showturtle
form = _turtle.shape
stempel = _turtle.stamp
stempel_loeschen = _turtle.clearstamp
breite = _turtle.width

# Fenster und Bildschirm
fensterfarbe = _turtle.bgcolor
titel = _turtle.title
warte = _turtle.done
aktualisieren = _turtle.update
verzoegerung = _turtle.delay
bildschirm = _turtle.Screen
hauptturtle = _turtle.Turtle

# Tastatur und Maus
taste = _turtle.onkey
taste_binden = _turtle.onkeypress
mausklick = _turtle.onclick
timer = _turtle.ontimer


# ==========================================
# Mensch: Zeichnet eine Strichfigur
# ==========================================

def Mensch(x=0, y=0, groesse=40, farbe="black"):
    """
    Zeichnet eine Strichfigur.

    x, y:      Position der Füße
    groesse:   Größe der Figur
    farbe:     Zeichenfarbe
    """
    t = _turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pensize(max(1, groesse / 20))
    t.pencolor(farbe)

    s = groesse
    kopf_r = 0.35 * s

    def linie(x1, y1, x2, y2):
        t.penup()
        t.goto(x + x1 * s, y + y1 * s)
        t.pendown()
        t.goto(x + x2 * s, y + y2 * s)

    # Kopf
    t.penup()
    t.goto(x, y + 2.15 * s)
    t.setheading(0)
    t.pendown()
    t.circle(kopf_r)

    # Körper
    linie(0, 2.15, 0, 0.9)

    # Arme
    linie(-0.75, 1.8, 0, 1.8)
    linie(0, 1.8, 0.75, 1.8)

    # Beine
    linie(0, 0.9, -0.65, 0)
    linie(0, 0.9, 0.65, 0)

    t.penup()
    t.hideturtle()
    return t


# ==========================================
# Beispiel
# ==========================================

if __name__ == "__main__":
    titel("Deutsche Turtle")

    geschwindigkeit(5)
    stiftgroesse(3)

    Mensch(-100, -100, 10)

    warte()

 