def find_max(nums, biggest_num=None):
    if len(nums) == 0:
        return biggest_num
    if biggest_num is None or nums[0] > biggest_num:
        biggest_num = nums[0]

    return find_max(nums[1:], biggest_num)
import turtle
def s(t: turtle.Turtle, segments, size, angle):
    t.pendown()
    for i in range(1, segments+1):
        t.fd(size*i)
        t.left(angle)

def draw_spiral_recursion(pen: turtle.Turtle, segments, size, angle, level=1):
    pen.pendown()
    if level < (segments + 1):
        pen.fd(size * level)
        pen.left(angle)
        draw_spiral_recursion(pen, segments, size, angle, level + 1)

