"""Anarchy
 
Grouping together functions that use chaos game and generate
points inside a fractal
I called this module chaos_gens earlier but anarchy is clearly better
"""

from utils import *


# generates points for a Sierpinski triangle, using chaos game,
# with it's centroid at (x0, y0), side length being slen, and
# number of points being npts
def gen_triangle_pts(x0, y0, slen, npts):
    inradius = 0.5*slen/(3**0.5)            # the triangle's inradius

    # p1, p2, p3 -> vertices of the triangle
    p1 = (x0 - slen/2, y0 - inradius)
    p2 = (x0 + slen/2, y0 - inradius)
    p3 = (x0, y0 + 2*inradius)
    pts_list = [p1, p2, p3]             # points which the accumulator can use to "jump"

    # the initial point is a random point inside the incircle
    acc_pt = rand_circ(x0, y0, inradius)    # acc_pt -> accumulator point
    out_pts = [acc_pt]                      # list of output points

    # generating the remaining npts-1 points using chaos game
    for i in range(npts-1):
        # acc_pt jumps halfway towards any random vertex
        acc_pt = midpoint_2d(acc_pt, random.choice(pts_list))
        out_pts.append(acc_pt)

    return out_pts


# generates point for a Sierpinski Christmas tree, which consists
# of `levels` Sierpinski triangles, stacked atop one another, with the
# bottom-most's centroid being (x0, y0) and the number of points in each
# of the triangles being npts
def gen_tree_pts(x0, y0, slen, levels, npts):
    out_pts = []
    delta_y = 0.125*slen*(3**0.5)       # the height delta between successive levels

    # updating the output points with points of the triangles
    for i in range(levels):
        y = y0 + i*delta_y
        out_pts += gen_triangle_pts(x0, y, slen, npts)

    return out_pts


# generating points for a Sierpinski carpet, using chaos game
# (x0, y0) is the centre of the carpet, l and w are it's length and
# and width, and npts are the number of points inside it
def gen_carpet_pts(x0, y0, l, w, npts):
    # p1 through p4 -> vertices of the square
    # p5 through p8 -> midpoints of edges of the square
    p1 = (x0 - l/2, y0 + w/2)
    p2 = (x0 + l/2, y0 + w/2)
    p3 = (x0 + l/2, y0 - w/2)
    p4 = (x0 - l/2, y0 - w/2)
    p5 = midpoint_2d(p1, p2)
    p6 = midpoint_2d(p2, p3)
    p7 = midpoint_2d(p3, p4)
    p8 = midpoint_2d(p4, p1)
    # points for the accumulator to use to jump
    pts_list = [p1, p2, p3, p4, p5, p6, p7, p8]

    # accumulator point : initially a random point in the rectangle
    acc_pt = rand_rect(*p4, l, w)
    out_pts = [acc_pt]      # list of output points

    # generating the remaining npts-1 points using chaos game
    for i in range(npts - 1):
        # acc_pt jumps 2/3 of the way towards a random vertex or edge midpoint
        acc_pt = ratio_div_2d(acc_pt, random.choice(pts_list), 2/3)
        out_pts.append(acc_pt)

    return out_pts


# generates points for a Vicsek fractal, with (x0, y0) as the centre,
# slen being the square's side length, angle being it's angular offset
# and npts being the number of points inside it
def gen_vicsek_pts(x0, y0, slen, angle, npts):
    # inradius and circumradius of the square
    inradius = slen/2
    circum_radius = slen/(2**0.5)

    # the square's vertices and centroid
    p1 = polar_sum((x0, y0), circum_radius, pi/4 + angle)
    p2 = polar_sum((x0, y0), circum_radius, 3*pi/4 + angle)
    p3 = polar_sum((x0, y0), circum_radius, 5*pi/4 + angle)
    p4 = polar_sum((x0, y0), circum_radius, 7*pi/4 + angle)
    p5 = midpoint_2d(p1, p3)
    # points for the accumulator to use to jump
    pts_list = [p1, p2, p3, p4, p5]

    # accumulator point : initially a random point in the incircle
    acc_pt = rand_circ(x0, y0, inradius)
    out_pts = [acc_pt]          # list of output points

    # generating the remaining npts-1 points using chaos game
    for i in range(npts-1):
        # acc_pt jumps 2/3 of the way towards a random vertex or the centroid
        acc_pt = ratio_div_2d(acc_pt, random.choice(pts_list), 2/3)
        out_pts.append(acc_pt)

    return out_pts

