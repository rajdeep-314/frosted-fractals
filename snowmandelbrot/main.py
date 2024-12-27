# Mandelbrot set

import pygame
from utils import *

# pygame initialization
pygame.init()
width = 1850
height = 1000
surf = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sierpinski Tree")
surf.fill((0,0,0))      # black background

# some global parameters
scale = 420                 # one unit on R = `scale` pixels


def k_factor(z, max_iter, inf):
    z0 = z
    for i in range(max_iter):
        if abs(z) >= inf:
            return i/(max_iter-1)
        z = z**2 + z0
    return 1
    

def gen_mandelbrot_pts(x1, x2, y1, y2, delta, max_iter = 50, inf = 10):
    x_pts = int((x2-x1)/delta)
    y_pts = int((y2-y1)/delta)
    pts_list = [complex(x1+i*delta, y1+j*delta) for i in range(x_pts) for j in range(y_pts)]
    kfs_list = [k_factor(z, max_iter, inf) for z in pts_list]
    return (pts_list, kfs_list)
        

# plot points inside pts_list, by lighting up pixels at
# those coordinates. color_func decides the color
def plot_pts(pts_list, kfs_list, map_func = lambda pt : pt, color_func = lambda r : (255,255,255)):
    for pt, k in zip(pts_list, kfs_list):
        x, y = map_func(pt)
        col = color_func(k)
        surf.set_at((int(x), int(y)), col)

# color maps
grayscale1 = linear_gradient((black, white))
grayscale2 = linear_gradient((white, black))
rainbow = linear_gradient((red, orange, yellow, green, blue, indigo, violet), special_col = black)
fire = linear_gradient(((59,14,0), orange), special_col = black)
ice = linear_gradient(((0,0,50), blue, white), special_col = black)

def map_func(pt):
    x = pt.real
    y = pt.imag
    return (width/2 + scale*y, height + scale*(x-0.4))
        

pts, ks = gen_mandelbrot_pts(-1.45,0.4,-1.2,1.2,0.01)
plot_pts(pts, ks, map_func, ice)


# displaying the surface and keeping the display running
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()

