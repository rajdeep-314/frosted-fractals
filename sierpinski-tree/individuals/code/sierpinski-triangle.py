import sys
sys.path.insert(1, sys.path[0] + "/../..")

import pygame
from anarchy import *

# pygame initialization
pygame.init()
width = 1920
height = 1080
surf = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sierpinski Triangle")
surf.fill((0,0,0))          # a black background


# plot points inside pts_list, by lighting up pixels at
# those coordinates. color_func decides the color based on
# the points' coordinates
def plot_pts(pts_list, color_func = lambda pt : (255,255,255), surface = surf):
    for pt in pts_list:
        pt = (int(pt[0]), height - int(pt[1]))      # integer coordinates and y-coordinate flipping
        surface.set_at(pt, color_func(pt))


# points for the Sierpinski triangle and the color function for it
triangle_pts = gen_triangle_pts(width/2, height/2 - 100, 1000, 1000000)
col_func = circ_gradient(width/2, height/2 + 100, (red, blue, green), 750, offset=pi/6)
plot_pts(triangle_pts, col_func, surf)


# displaying the surface
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()

