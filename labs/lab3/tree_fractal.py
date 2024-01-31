import time
import turtle as t


def set_canvas():
    s = t.Screen()
    s.setup(450, 410)
    s.bgcolor('ivory')
    s.title('Turtle Program')
    return s


# set a turtle (a pen)
def set_pen(color):
    pen = t.Turtle()
    pen.shape('turtle')
    pen.pen(pencolor=color, fillcolor=color, pensize=1, speed=10)
    return pen

def draw_tree(pen: t.Turtle, branch_size, angle, n):
    draw_tree_helper(pen, branch_size, branch_size, angle, n, True)

# draw a tree fractal using recursion
def draw_tree_helper(pen: t.Turtle, branch_size, branch_width, angle, n, is_left_side: bool):
    if n > 0:  # recursive step
        right_pen = pen.clone()

        right_pen.penup()

        (right_pen.right if is_left_side else right_pen.left) (90)
        right_pen.fd(branch_width)
        (right_pen.left if is_left_side else right_pen.right) (90)
        right_pen.pendown()

        if not is_left_side:
            right_pen, pen = pen, right_pen

        pen.pen(pensize=2)

        pen.fd(branch_size)
        right_pen.fd(branch_size)

        pen.left(angle)
        right_pen.right(angle)

        pen.pen(pensize=1)

        draw_tree_helper(pen, branch_size / 2, branch_width / 2, angle, n - 1, True)
        draw_tree_helper(right_pen, branch_size, branch_width / 2, angle, n - 1, False)
        right_pen.hideturtle()

    else:  # base case
        draw_leaves(pen)



def draw_leaves(pen):
    original_col = pen.pencolor(), pen.fillcolor()
    pen.pen(pencolor='green', fillcolor='green')
    pen.begin_fill()
    pen.circle(10)
    pen.end_fill()
    pen.pen(pencolor=original_col[0], fillcolor=original_col[1])
