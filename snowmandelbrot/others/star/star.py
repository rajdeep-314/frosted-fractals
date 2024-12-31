# NOTE: Just for showcasing, not part of the main submission

import sys
sys.path.insert(1, sys.path[0] + "/../..")

import pygame
from utils import *


# pygame initialization
pygame.init()
width = 10000
height = 10000
surf = pygame.display.set_mode((width, height))
pygame.display.set_caption("Star")
surf.fill((0,0,0))      # black background


# plot points inside pts_list, by lighting up pixels at
# those coordinates. color_func decides the color based on
# the points' coordinates
def plot_pts(pts_list, color_func = lambda pt : (255,255,255), surface = surf):
    for pt in pts_list:
        pt = (int(pt[0]), height - int(pt[1]))      # integer coordinates and y-coordinate flipping
        surface.set_at(pt, color_func(pt))


# the star's points and color function
star_pts = gen_star_pts(width/2, height/2, 5300, 10000000)
col_func = circ_gradient(width/2, height/2, (red, green, blue), 5000)
plot_pts(star_pts, col_func, surf)

pygame.image.save(surf, "star-chaos.png")
print("\nDone saving")

