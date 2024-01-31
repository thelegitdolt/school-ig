# draws a tree
import turtle


# set the canvas window
def set_canvas():
    s = turtle.Screen()
    s.setup(450, 410)
    s.bgcolor('ivory')
    s.title('Turtle Program')
    return s


# set a turtle (a pen)
def set_pen(color):
    t = turtle.Turtle()
    t.shape('turtle')
    t.pen(pencolor=color, fillcolor=color, pensize=1, speed=10)
    return t


# draw a tree fractal using recursion



# main program
if __name__ == '__main__':
    s = set_canvas()
    t = set_pen('brown')
    t.penup()
    t.goto(-45, -150)
    t.left(90)
    t.pendown()

    from labs.lab3.tree_fractal import draw_tree
    draw_tree(t, 60, 20, 6)
    s.exitonclick()
