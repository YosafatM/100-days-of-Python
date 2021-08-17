def solid_line(turtle, size):
    turtle.forward(size)


def dashed_line(turtle, size):
    pace = int(size / 10)

    for _ in range(1, 10):
        turtle.forward(pace)
        turtle.pen(pendown=not turtle.isdown())


def regular_shape(turtle, size, num_sizes, line=solid_line):
    angle = 360 / num_sizes

    for _ in range(1, num_sizes+1):
        line(turtle, size)
        turtle.right(angle)
