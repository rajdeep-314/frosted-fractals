import math
import pygame
import random
from utils import *


# pygame initialization
pygame.init()
width = 1729            # smallest Ramanujan number
height = 942            # floor(300pi)
surf = pygame.display.set_mode((width, height))
surf.fill((0,0,0))

def gen_triangle_pts(x0, y0, slen, npts):
    inradius = 0.5*slen/(3**0.5)
    rand_r = random.random()*inradius
    rand_theta = random.random()*2*math.pi
    acc_pt = (x0 + rand_r*math.cos(rand_theta), y0 + rand_r*math.sin(rand_theta))
    
    p1 = (x0 - slen/2, y0 - inradius)
    p2 = (x0 + slen/2, y0 - inradius)
    p3 = (x0, y0 + 2*inradius)
    pts_list = [p1, p2, p3]
    out_pts = [acc_pt]

    for i in range(npts-1):
        acc_pt = midpoint_2d(acc_pt, random.choice(pts_list))
        out_pts.append(acc_pt)

    return out_pts

def gen_carpet_pts(x0, y0, slen, npts):
    p1 = (x0 - slen/2, y0 + slen/2)
    p2 = (x0 + slen/2, y0 + slen/2)
    p3 = (x0 + slen/2, y0 - slen/2)
    p4 = (x0 - slen/2, y0 - slen/2)
    p5 = midpoint_2d(p1, p2)
    p6 = midpoint_2d(p2, p3)
    p7 = midpoint_2d(p3, p4)
    p8 = midpoint_2d(p4, p1)

    # accumulator point
    acc_pt = rand_rect(*p4, slen, slen)
    pts_list = [p1, p2, p3, p4, p5, p6, p7, p8]
    out_pts = [acc_pt]

    for i in range(npts - 1):
        acc_pt = ratio_div_2d(acc_pt, random.choice(pts_list), 2/3)
        out_pts.append(acc_pt)
    return out_pts

def plot_pts(pts_list, color_func = lambda pt : (255,255,255), surface = surf):
    for pt in pts_list:
        pt = (int(pt[0]), height - int(pt[1]))      # integer coordinates and y-coordinate flipping
        surface.set_at(pt, color_func(pt))


pts = gen_triangle_pts(width/2, height/2 - 100, 750, 500000)

# Christmas themed color function - based on red, green and white colors
chris_col_func = circ_gradient(width/2, height/2 + 100, (white, red, green, blue, white, red, green, blue), 350)
plot_pts(pts, chris_col_func)

# displaying the surface
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()

