def draw_spiral(pen, segments, size, angle, level=1):
    pen.pendown()
    if level < (segments + 1):
        pen.fd(size * level)
        pen.left(angle)
        draw_spiral(pen, segments, size, angle, level + 1)
