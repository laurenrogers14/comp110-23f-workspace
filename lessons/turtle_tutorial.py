"""Practice with turtle."""

from turtle import Turtle, colormode, done

leo: Turtle = Turtle()

i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    leo.pencolor("pink")
    leo.speed(50)
    leo.hideturtle()
    i = i + 1
done()