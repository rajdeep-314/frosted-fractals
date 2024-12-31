"""main.py

Running it should open a window of near-HD resolution. The image should be rendered roughly in a minute. The terminal displays a progress bar to denote how much calculation has been performed for the Mandelbrot set. Do note though that this doesn't say anything about the time taken to plot all those points.
"""

import pygame
from utils import *

# pygame initialization
pygame.init()
# the screen's resolution
width = 1850
height = 1000
surf = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snowmandelbrot")
surf.fill((0,0,0))      # black background

scale = 375                 # one unit on the real number line = `scale` pixels


# this real number is equal to the number of iterations of
# the Mandelbrot formula (z_{n+1} = z_{n}^2 + z_0), after which
# the point z goes outside inf (i.e. |z| > inf), divided by max_iter
# for a point that never goes outside inf, it returns 1
def k_factor(z, max_iter, inf):
    z0 = z
    for i in range(int(max_iter)):
        if abs(z) > inf:
            return i/(max_iter-1)
        z = z**2 + z0
    return 1


# returns two lists in a tuple, say (p, k), where
# p are all the points (x, y) such that x1 <= x <= x2 and y1 <= y <= y2,
# sampled at differences of delta
# k is the list of the k-factors for these points, evaluated with
# max_iter and inf as it's parameters
# if show_status is True, the progress of these calculations is printed
def gen_mandelbrot_pts(x1, x2, y1, y2, delta, max_iter = 100, inf = 10, show_status = False):
    x_pts = int((x2-x1)/delta)              # no. of points along the grid's length
    y_pts = int((y2-y1)/delta)              # no. of points along the grid's width
    total_pts = x_pts * y_pts               # no. of total points in the grid
    pts_list = []                           # the list p, from the comment before the function

    # if show_status is set to True, display the progress
    if show_status:
        print("\n\n")
        for i in range(x_pts):
            for j in range(y_pts):
                progress = i*y_pts + j + 1
                print("\rMandelbrot calculation progress: " + "#"*int((progress/total_pts)*50) + "-"*int((1 - progress/total_pts)*50), end = "")
                pts_list.append(complex(x1+i*delta, y1+j*delta))

    # if show_status is False, the calculations are faster,
    # as list comprehension is used instead of two nested for loops
    else:
        pts_list = [complex(x1+i*delta, y1+j*delta) for i in range(x_pts) for j in range(y_pts)]

    # this list is k, from the comment before the function
    kfs_list = [k_factor(z, max_iter, inf) for z in pts_list]

    # print a new line if show_status is True
    if show_status:
        print()

    return (pts_list, kfs_list)


# plot points inside pts_list, by lighting up pixels at
# those coordinates. color_func decides the color based on
# the points' coordinates
def plot_pts(pts_list, color_func = lambda pt : (255,255,255), surface = surf):
    for pt in pts_list:
        pt = (int(pt[0]), height - int(pt[1]))      # integer coordinates and y-coordinate flipping
        surface.set_at(pt, color_func(pt))


# plot points inside pts_list, by lighting up pixels at
# those coordinates. color_func decides the color based on
# the k-factor inside kfs_list
def plot_mandel_pts(pts_list, kfs_list, map_func = lambda pt : pt, color_func = lambda r : (255,255,255), surface = surf):
    for pt, k in zip(pts_list, kfs_list):
        x, y = map_func(pt)
        col = color_func(k)
        surface.set_at((int(x), int(y)), col)


# mapping a point in the Cartesian plane to the screen,
# this gives the Mandelbrot set the snowman-like orientation
def map_func(pt):
    x = pt.real
    y = pt.imag
    return (width/2 + scale*y, height + scale*(x-0.4))
        

# points for the mandelbrot set
pts, ks = gen_mandelbrot_pts(-2.26666,0.4,-2.46666,2.46666,0.0022, max_iter = 250, show_status = True)

# points for the cap and star atop the Snowmandelbrot
cap_pts = gen_triangle_pts(width/2, 0.685*height, 0.225*height, 100000)
star_pts = gen_star_pts(width/2, 0.87*height, 0.065*height, 10000, pi)

# plotting all the generated points
plot_mandel_pts(pts, ks, map_func, snow, surface=surf)
plot_pts(cap_pts, lambda pt : (255,0,0), surface=surf)
plot_pts(star_pts, surface=surf)


# displaying the surface and keeping the display running
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()

