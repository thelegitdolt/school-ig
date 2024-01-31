# draws a Sierpinski triangle
import turtle


# set canvas
def set_canvas():
    s = turtle.Screen()
    s.setup(450, 450)
    turtle.bgcolor("ivory")
    turtle.title("Sierpinski Triangle")
    return s


# set a turtle (a pen)
def set_pen(color):
    t = turtle.Turtle()
    t.shape("turtle")
    t.pen(pencolor=color, fillcolor=color, pensize=1, speed=5)
    return t


# draw a triangle
def draw_triangle(vertices, color, my_turtle):
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(vertices[0][0], vertices[0][1])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(vertices[1][0], vertices[1][1])
    my_turtle.goto(vertices[2][0], vertices[2][1])
    my_turtle.goto(vertices[0][0], vertices[0][1])
    my_turtle.end_fill()


# find the midpoint
def midpoint(point1, point2):
    return [(point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2]


# draw Sierpinski triangle recursively
def draw_sierpinski(vertices, level, my_turtle):
    global colors
    if level > 0:  # recursive step
        draw_triangle(vertices, colors[level], my_turtle)  # this is optional
        draw_sierpinski([vertices[0],
                         midpoint(vertices[0], vertices[1]),
                         midpoint(vertices[0], vertices[2])],
                        level - 1, my_turtle)
        draw_sierpinski([vertices[1],
                         midpoint(vertices[0], vertices[1]),
                         midpoint(vertices[1], vertices[2])],
                        level - 1, my_turtle)
        draw_sierpinski([vertices[2],
                         midpoint(vertices[2], vertices[1]),
                         midpoint(vertices[0], vertices[2])],
                        level - 1, my_turtle)
    else:  # base case
        draw_triangle(vertices, colors[level], my_turtle)


# main program
s = set_canvas()
t = set_pen("black")
t.left(90)
colors = ["red", "gold", "aqua", "navy", "cadet blue"]
vertices = [[-200, -100], [0, 200], [200, -100]]
draw_sierpinski(vertices, 4, t)
s.exitonclick()

