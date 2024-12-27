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
    total_pts = x_pts * y_pts
    pts_list = []
    print("\n\n")
    for i in range(x_pts):
        for j in range(y_pts):
            progress = i*y_pts + j + 1
            print("\rProgress: " + "#"*int((progress/total_pts)*50) + "-"*int((1 - progress/total_pts)*50), end = "")
            pts_list.append(complex(x1+i*delta, y1+j*delta))
    # pts_list = [complex(x1+i*delta, y1+j*delta) for i in range(x_pts) for j in range(y_pts)]
    kfs_list = [k_factor(z, max_iter, inf) for z in pts_list]
    print()
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
snow = linear_gradient(((0,20,20), cyan, cyan, cyan, cyan), special_col = white)

def map_func(pt):
    x = pt.real
    y = pt.imag
    return (width/2 + scale*y, height + scale*(x-0.4))
        

pts, ks = gen_mandelbrot_pts(-1.97,0.4,-2.2,2.2,0.001, max_iter = 1000, inf = 25)
plot_pts(pts, ks, map_func, snow)

pygame.image.save(surf, "snowmandelbrot/images/snow-alt-2.png")
print("Done saving")

