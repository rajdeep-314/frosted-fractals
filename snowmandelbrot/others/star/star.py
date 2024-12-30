# NOTE: Just for showcasing, not part of the main submission

import pygame
from utils import *


# pygame initialization
pygame.init()
width = 10000
height = 10000
surf = pygame.display.set_mode((width, height))
pygame.display.set_caption("Star")
surf.fill((0,0,0))      # black background


def plot_pts(pts_list, color_func = lambda pt : (255,255,255), surface = surf):
    for pt in pts_list:
        pt = (int(pt[0]), height - int(pt[1]))      # integer coordinates and y-coordinate flipping
        surface.set_at(pt, color_func(pt))

def gen_star_pts(x0, y0, slen, npts, angle = 0):
    circum_radius = 0.5*slen/math.sin(pi/5)
    inradius = 0.5*slen*math.tan(pi/5)
    p1 = polar_sum((x0, y0), circum_radius, pi/10 + angle)
    p2 = polar_sum((x0, y0), circum_radius, pi/10 + 2*pi/5 + angle)
    p3 = polar_sum((x0, y0), circum_radius, pi/10 + 4*pi/5 + angle)
    p4 = polar_sum((x0, y0), circum_radius, pi/10 + 6*pi/5 + angle)
    p5 = polar_sum((x0, y0), circum_radius, pi/10 + 8*pi/5 + angle)
    pts_list = [p1, p2, p3, p4, p5]

    last = None
    second_last = None
    # the accumulator point
    acc_pt = rand_circ(x0, y0, inradius)
    out_pts = [acc_pt]

    for i in range(npts):
        if last == second_last and last is not None:
            new = random.choice(remove_neighbours(5, last))
        else:
            new = random.choice(range(5))
        last, second_last = new, last
        acc_pt = midpoint_2d(acc_pt, pts_list[new])
        out_pts.append(acc_pt)
    return out_pts

col_func = circ_gradient(width/2, height/2, (red, green, blue), 5000)

pts = gen_star_pts(width/2, height/2, 5300, 10000000)
plot_pts(pts, col_func)

pygame.image.save(surf, "star-chaos.png")
print("\nDone saving")

