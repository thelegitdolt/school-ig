import turtle as t


def get_points(x, y, size, sides):
    yield x, y

    traverser = t.Turtle()
    traverser.hideturtle()
    traverser.penup()
    traverser.pen(speed=1000)

    # set up new turtle to draw position
    traverser.goto(x, y)
    traverser.left(90)
    traverser.fd(size)

    angle = 360 / sides
    for i in range(sides - 1):
        traverser.left(180 + angle)
        traverser.fd(size)
        yield traverser.xcor(), traverser.ycor()
        traverser.left(180)
        traverser.fd(size)




def star(size, sides, pen: t.Turtle, d=2):
    pen.pendown()
    points = tuple(get_points(pen.xcor(), pen.ycor(), size, sides))
    new_index = 0
    for i in range(sides):
        new_index = (new_index + d) % sides
        pen.goto(points[new_index])
    t.penup()


def star_recursive_helper(size, sides, pen: t.Turtle, points, current_index, d, level):
    if level > 0:
        current_index = (current_index + d) % sides
        pen.goto(points[current_index])
        star_recursive_helper(size, sides, pen, points, current_index, d, level - 1)


def star_recursive(size, sides, level, pen: t.Turtle, d=2):
    t.pendown()
    star_recursive_helper(size, sides, pen, tuple(get_points(pen.xcor(), pen.ycor(), size, sides)), 0, d, sides)
    t.penup()

