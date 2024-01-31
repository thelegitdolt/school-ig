import turtle as t

def polygon(size, sides, pen: t.Turtle):
    pen.pendown()
    angle = (180 * (sides - 2)) / sides
    for side in range(sides):
        pen.left(180 - angle)
        pen.fd(size)

    pen.penup()

def polygon_recursive(size, sides, level, pen: t.Turtle):
    angle = (180 * (sides - 2)) / sides
    if sides == level:
        pen.pendown()

    if level <= 0:
        pen.penup()
    else:
        pen.left(180 - angle)
        pen.fd(size)
        polygon_recursive(size, sides, level - 1, pen)
