# Anarchy
# 
# Grouping together functions that use chaos game and generate
# points inside a fractal
# I called this module chaos_gens earlier but anarchy is better

from utils import *


# generating points for a Sierpinski triangle, using chaos game,
# with it's centroid at (x0, y0) side length being slen, and
# number of points being npts
def gen_triangle_pts(x0, y0, slen, npts):
    inradius = 0.5*slen/(3**0.5)

    # the initial point is a random point inside the incircle
    rand_r = random.random()*inradius
    rand_theta = random.random()*2*math.pi

    # accumulator point : (rand_r, rand_theta) in polar coordinates, with (x0, y0) as origin
    acc_pt = (x0 + rand_r*math.cos(rand_theta), y0 + rand_r*math.sin(rand_theta))
    
    # p1, p2, p3 -> vertices of the triangle
    p1 = (x0 - slen/2, y0 - inradius)
    p2 = (x0 + slen/2, y0 - inradius)
    p3 = (x0, y0 + 2*inradius)
    pts_list = [p1, p2, p3]

    out_pts = [acc_pt]      # output points
    for i in range(npts-1):
        acc_pt = midpoint_2d(acc_pt, random.choice(pts_list))
        out_pts.append(acc_pt)

    return out_pts


def gen_tree_pts(x0, y0, slen, levels, npts):
    out_pts = []
    delta_y = 0.125*slen*(3**0.5)
    for i in range(levels):
        y = y0 + i*delta_y
        out_pts += gen_triangle_pts(x0, y, slen, npts)
    return out_pts

# generating points for a Sierpinski carpet, using chaos game,
# (x0, y0) is the centre of the carpet, slen is the side length
# and npts are the number of points inside it
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
    pts_list = [p1, p2, p3, p4, p5, p6, p7, p8]

    # accumulator point : initially a random point in the square
    acc_pt = rand_rect(*p4, l, w)

    out_pts = [acc_pt]      # output points
    for i in range(npts - 1):
        acc_pt = ratio_div_2d(acc_pt, random.choice(pts_list), 2/3)
        out_pts.append(acc_pt)

    return out_pts


def gen_vicsek_pts(x0, y0, slen, angle, npts):
    inradius = slen/2
    circum_radius = slen/(2**0.5)
    p1 = polar_sum((x0,y0), circum_radius, pi/4 + angle)
    p2 = polar_sum((x0,y0), circum_radius, 3*pi/4 + angle)
    p3 = polar_sum((x0,y0), circum_radius, 5*pi/4 + angle)
    p4 = polar_sum((x0,y0), circum_radius, 7*pi/4 + angle)
    p5 = midpoint_2d(p1, p3)
    pts_list = [p1, p2, p3, p4, p5]

    # accumulator point
    acc_pt = polar_sum((x0,y0), random.random()*inradius, random.random()*2*pi)

    out_pts = [acc_pt]
    for i in range(npts-1):
        acc_pt = ratio_div_2d(acc_pt, random.choice(pts_list), 2/3)
        out_pts.append(acc_pt)

    return out_pts


