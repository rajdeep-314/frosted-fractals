# Sierpinski tree
# The leaves are Sierpinksi triangles, made using recursion and
# turtle commmands. The trunk is a Sierpinksi carpet, the points
# of which have been evaluated using chaos game, and plotted
# using turtle. Read more about chaos game here:
# https://en.wikipedia.org/wiki/Chaos_game

import math
import turtle
from utils import *

# Uncomment this if turtle.teleport is not defined (added in v3.12)
# def teleport(x, y):
#     turtle.penup()
#     turtle.setpos(x, y)
#     turtle.pendown()
# turtle.teleport = teleport

# Some visual initialization
turtle.bgcolor('black')
turtle.hideturtle()
turtle.speed(10)
turtle.width(2)

# Sierpinksi triangle of length `len`, starting at the current position
# align = True -> the current position will be the centroid
# this function is recursive on `order`
def triangle(len, order, align = False, color_func = None):
    if align == True:
        # going to the starting position
        turtle.teleport(turtle.xcor() - len/2, turtle.ycor() - (3**0.5)*len/6)
        return triangle(len, order, align = False, color_func = color_func)

    # color
    if color_func is not None:
        turtle.pencolor(color_func(turtle.pos()))

    # the base case - a simple triangle
    if order == 0:
        for i in range(3):
            turtle.fd(len)
            turtle.lt(120)
        turtle.fd(len)
        return

    # the recursive step - drawing 3 triangles of order `order-1`
    for i in range(3):
        triangle(len/2, order-1, align = False, color_func = color_func)
        for j in [range(0), range(1), range(1)][i]:
            turtle.lt(120)
            turtle.fd(len/2)
    # adjusting the terminating position, to complete the recursive step
    turtle.fd(len/2)
    turtle.lt(120)
    turtle.fd(len)

# draws a christmas tree, consisting of `levels` Sierpinksi triangles,
# stacked on top of each other, using recursion on `levels`
def tree(len, order, levels, align = True, color_func = None):
    if (levels < 0):
        raise Exception("The levels must be a postiive integer")
    
    # the base triangle
    triangle(len, order, align = align, color_func = color_func)

    # base case for recursion
    if levels == 1:
        return

    # the recursive step
    turtle.teleport(turtle.xcor() - len, turtle.ycor() + (3**0.5)*len/8)
    tree(len, order, levels-1, align = False, color_func = color_func)
        
# Generates points in a Sierpinski carpet, centered
# at (x0, y0), of dimensions (len x len)
# Chaos game is used to generate these points, pseudo-randomly
def carpet_pts(x0, y0, len, n_pts, show_status = False):
    p1 = (x0 - len/2, y0 + len/2)
    p2 = (x0 + len/2, y0 + len/2)
    p3 = (x0 + len/2, y0 - len/2)
    p4 = (x0 - len/2, y0 - len/2)
    p5 = midpoint_2d(p1, p2)
    p6 = midpoint_2d(p2, p3)
    p7 = midpoint_2d(p3, p4)
    p8 = midpoint_2d(p4, p1)

    # accumulator point
    acc_pt = rand_rect(*p4, len, len)
    pts_list = [p1, p2, p3, p4, p5, p6, p7, p8]
    out_pts = [acc_pt]

    if show_status:
        print("Sierpinski carpet points generation - progress:\n")

    for i in range(n_pts - 1):
        if show_status:
            progress = int(50 * i/(n_pts - 2))
            print('\r' + progress*'#' + (50-progress)*'-', end = '')
        acc_pt = ratio_div_2d(acc_pt, random.choice(pts_list), 2/3)
        out_pts.append(acc_pt)

    if show_status:
        print("\nGeneration complete\n")
    return out_pts


# DRAWING BEGIN
turtle.tracer(0)

# Position initialization
turtle.teleport(0, -120)

# Christmas themed color function - based on red, green and white colors
chris_col_func = circ_gradient2(0, 50, (1,1,1), (0,1,0), (1,0,0), 240, offset = 0)

# Generating the leaves of the tree
tree(600, 7, 3, color_func = chris_col_func)

# Generating the trunk, a Sierpinski carpet with 40,000 points
turtle.pencolor(0.5, 0, 0)
pts = carpet_pts(0, -400, 210, 40000, show_status = True)
plot_pts(pts)

# DRAWING END
turtle.tracer(1)
turtle.mainloop()
