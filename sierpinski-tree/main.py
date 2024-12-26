import math
import pygame
import random
from utils import *


# pygame initialization
pygame.init()
width = 1850
height = 1000
surf = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sierpinski Tree")
surf.fill((0,0,0))      # black background

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


# plot points inside pts_list, by lighting up pixels at
# those coordinates. color_func decides the color
def plot_pts(pts_list, color_func = lambda pt : (255,255,255), surface = surf):
    for pt in pts_list:
        pt = (int(pt[0]), height - int(pt[1]))      # integer coordinates and y-coordinate flipping
        surface.set_at(pt, color_func(pt))


# Christmas themed color function - based on red, green and white colors
chris_col_func = circ_gradient(width/2, height/2 - 100, ((255,50,50), (0,175,255), (255,50,50), (0,200,0)), 300)

# generating the leaves and trunk
leaves_pts = gen_tree_pts(width/2, height/2 - 115, 590, 3, 300000)
trunk_pts = gen_carpet_pts(width/2, height/2 - 400, 175, 230, 100000)


# plotting on the surface
plot_pts(trunk_pts, lambda pt : (110,38,14))
plot_pts(leaves_pts, chris_col_func)


# displaying the surface and keeping the display running
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()

