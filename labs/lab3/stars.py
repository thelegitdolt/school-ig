import turtle as t

def star(size, sides, pen: t.Turtle, d=2):
    pen.pendown()
    angle = 180 / sides
    for side in range(sides):
        pen.right(180 - angle)
        pen.fd(size)

    pen.penup()


def star_recursive(size, sides, level, pen: t.Turtle, d=2):
    pass
