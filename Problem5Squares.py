# Seil Tekinaeva
# March 4, 2026
# Problem 5: Draw multiple growing squares using turtle

import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")
alex.speed(0)

step = 30          # how much bigger each square gets
count = 5          # how many squares
size = step        # starting size

for i in range(count):
    # Move to the bottom-left corner so the square is centered at (0,0)
    alex.penup()
    alex.goto(-size/2, -size/2)
    alex.setheading(0)
    alex.pendown()

    drawSquare(alex, size)
    size += step

wn.exitonclick()
