# snowflake test

import pygame
from utils import *

# pygame initialization
pygame.init()
width = 800
height = 600
surf = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snowflake")
surf.fill((0,0,0))      # black background


# work on this
def draw_koch_segment(x0, y0, slen, angle, order, col_func = lambda pt : (255,255,255), width = 1):
    if order == 0:
        pygame.draw.line(surf, col_func((x0,y0)), (x0, height-y0), polar_sum((x0, height-y0), slen, -angle), width = width)
        return
    pt = (x0, y0)
    for phi in [0, pi/3, -pi/3, 0]:
        draw_koch_segment(*pt, slen/3, angle + phi, order-1, col_func, width = width)
        pt = polar_sum(pt, slen/3, angle + phi)
    
def draw_koch_snowflake(x0, y0, slen, angle, order, col_func = lambda pt : (255,255,255), width = 1):
    pt = polar_sum((x0, y0), slen/(3**0.5), 5*pi/6 + angle)
    for i in range(3):
        draw_koch_segment(*pt, slen, angle - 2*pi*i/3, order, col_func, width = width)
        pt = polar_sum(pt, slen, angle - 2*pi*i/3)


# chris_col_func = circ_gradient(width/2, height/2 - 100, ((255,50,50), (0,175,255), (255,50,50), (0,200,0)), 300)
chris_col_func = circ_gradient(400, 300, (white, cyan, blue)*4, 300)
draw_koch_snowflake(400, 300, 500, 0, 6, chris_col_func)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
