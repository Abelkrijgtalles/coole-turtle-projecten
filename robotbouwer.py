import random
import turtle

tina = turtle.Turtle()
tina.shape("turtle")

kleuren = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white"]

def rechthoek(horizontaal, verticaal, kleur):
    tina.pendown()
    tina.pensize(1)
    tina.color(kleur)
    tina.begin_fill()
    for teller in range(1, 3):
        tina.forward(horizontaal)
        tina.right(90)
        tina.forward(verticaal)
        tina.right(90)
    tina.end_fill()
    tina.penup()


tina.penup()
tina.speed("slow")

# voeten
tina.goto(-100, -150)
rechthoek(50, 20, random.choice(kleuren))
tina.goto(-30, -150)
rechthoek(50, 20, random.choice(kleuren))

# benen
tina.goto(-25, -50)
rechthoek(15, 100, random.choice(kleuren))
tina.goto(-55, -50)
rechthoek(-15, 100, random.choice(kleuren))

# lichaam
tina.goto(-90, 100)
rechthoek(100, 150, random.choice(kleuren))

# armen
tina.goto(-150, 70)
rechthoek(60, 15, random.choice(kleuren))
tina.goto(-150, 110)
rechthoek(15, 40, random.choice(kleuren))
tina.goto(10, 70)
rechthoek(60, 15, random.choice(kleuren))
tina.goto(55, 110)
rechthoek(15, 40, random.choice(kleuren))

# nek
tina.goto(-50, 120)
rechthoek(15, 20, random.choice(kleuren))

# hoofd
tina.goto(-85, 170)
rechthoek(80, 50, random.choice(kleuren))

# ogen
tina.goto(-60, 160)
rechthoek(30, 10, random.choice(kleuren))
tina.goto(-55, 155)
rechthoek(5, 5, random.choice(kleuren))
tina.goto(-40, 155)
rechthoek(5, 5, random.choice(kleuren))

# mond
tina.goto(-65, 135)
rechthoek(40, 5, random.choice(kleuren))
tina.hideturtle()

while True:
    tina.hideturtle()
