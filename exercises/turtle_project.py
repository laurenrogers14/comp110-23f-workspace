"""A depiction of a soccer field using code."""

__author__ = "730711512"
from turtle import Turtle, colormode, done
MAX_SPEED: int = 0
x: float
y: float

def main() -> None:
    """The entrypoint of my scene."""
    colormode(255)

    field: Turtle = Turtle()

    draw_rectangle(field, -250, -300)

    field_lines(field, -250, 20)

    draw_penalty_boxes(field, -100, 260)
    draw_penalty_boxes(field, -100, -300)

    draw_center_circle(field, -49, -25)

    draw_half_circle(field, -65, 205)
    draw_half_circle(field, -65, -200)

    done()


def draw_rectangle(rectangle: Turtle, x: float, y: float) -> None:
    "Draw the soccer field in the middle of the page."
    rectangle.penup()
    rectangle.goto(x, y)
    rectangle.pendown()
    rectangle.hideturtle()
    rectangle.speed(MAX_SPEED)
    rectangle.fillcolor("green")
    rectangle.begin_fill()
    i: int = 0
    while i < 2:
        rectangle.forward(500)
        rectangle.left(90)
        rectangle.forward(650)
        rectangle.left(90)
        i = i + 1
    rectangle.end_fill()
    rectangle.color("white")


def field_lines(lines: Turtle, x: float, y: float) -> None:
    "Draw the center line of the field inside the rectangle."
    lines.penup()
    lines.goto (x, y)
    lines.pendown()
    lines.forward(500)
    lines.color("white")
    lines.speed(MAX_SPEED)


def draw_penalty_boxes(rectangles: Turtle, x: float, y: float) -> None:
    "Draw penalty boxes on each side of the field."
    rectangles.penup()
    rectangles.goto(x, y)
    rectangles.pendown()
    rectangles.forward(200)
    rectangles.left(90)
    rectangles.forward(100)
    rectangles.left(90)
    rectangles.forward(200)
    rectangles.left(90)
    rectangles.forward(100)
    rectangles.left(90)
    rectangles.color("white")


def draw_center_circle(circle: Turtle, x: float, y: float) -> None:
    "Draw square in the middle of the field to be the center circle."
    circle.penup()
    circle.goto(x,y)
    circle.pendown()
    circle.color("white")
    i: int = 0
    while i < 4:
        circle.forward(100)
        circle.left(90)
        i = i + 1
        

def draw_half_circle(half_circle: Turtle, x: float, y: float) -> None:
    "Draw the semi circle at the top of each penalty box on each side of the field."
    half_circle.penup()
    half_circle.goto(x, y)
    half_circle.pendown()
    half_circle.forward(130)
    half_circle.left(90)
    half_circle.forward(55)
    half_circle.left(90)
    half_circle.forward(130)
    half_circle.left(90)
    half_circle.forward(55)
    half_circle.left(90)
    half_circle.color("white")
    

if __name__  == "__main__":
    main()



    
    





