import turtle
import random

window = turtle.Screen()

# Starting parameters
MAX_X = 50
MAX_Y = 50
initial_angle = random.randrange(15, 60)
speed = 10
nummer = 0

# Create a turtle and name it Bob.
tina = turtle.Turtle()
window.reset()
window.setworldcoordinates(-MAX_X,-MAX_Y,MAX_X,MAX_Y)
tina.left(initial_angle)
tina.speed(speed)
tina.pensize(10)
tina.shape("turtle")

def veranderkleur(nummer):
    kleuren = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
    tina.color(kleuren[nummer])
    nummer += 1
    if nummer == len(kleuren):
        nummer = 0
    return nummer

while True:
    xBob = tina.xcor()
    yBob = tina.ycor()
    print(xBob,yBob)
    if abs(xBob) >= MAX_X: # Use abs() to capture both walls
        heading = tina.heading()
        tina.setheading(180 - heading)
        nummer = veranderkleur(nummer)
    if abs(yBob) >= MAX_Y:
        heading = tina.heading()
        tina.setheading(-heading)
        nummer = veranderkleur(nummer)
    tina.fd(1)
window.exitonclick()