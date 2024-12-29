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
# scale = 420                 # one unit on R = `scale` pixels
scale = 375                 # one unit on R = `scale` pixels


def k_factor(z, max_iter, inf):
    z0 = z
    for i in range(int(max_iter)):
        if abs(z) >= inf:
            return i/(max_iter-1)
        z = z**2 + z0
    return 1
    
def gen_mandelbrot_pts(x1, x2, y1, y2, delta, max_iter = 100, inf = 10, show_status = False):
    x_pts = int((x2-x1)/delta)
    y_pts = int((y2-y1)/delta)
    total_pts = x_pts * y_pts
    pts_list = []
    if show_status:
        print("\n\n")
        for i in range(x_pts):
            for j in range(y_pts):
                progress = i*y_pts + j + 1
                print("\rMandelbrot calculation progress: " + "#"*int((progress/total_pts)*50) + "-"*int((1 - progress/total_pts)*50), end = "")
                pts_list.append(complex(x1+i*delta, y1+j*delta))
    else:
        pts_list = [complex(x1+i*delta, y1+j*delta) for i in range(x_pts) for j in range(y_pts)]
    kfs_list = [k_factor(z, max_iter, inf) for z in pts_list]
    if show_status:
        print()
    return (pts_list, kfs_list)


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


# plot points inside pts_list, by lighting up pixels at
# those coordinates. color_func decides the color
def plot_pts(pts_list, color_func = lambda pt : (255,255,255), surface = surf):
    for pt in pts_list:
        pt = (int(pt[0]), height - int(pt[1]))      # integer coordinates and y-coordinate flipping
        surface.set_at(pt, color_func(pt))


# plot points inside pts_list, by lighting up pixels at
# those coordinates. color_func decides the color
def plot_mandel_pts(pts_list, kfs_list, map_func = lambda pt : pt, color_func = lambda r : (255,255,255)):
    for pt, k in zip(pts_list, kfs_list):
        x, y = map_func(pt)
        col = color_func(k)
        surf.set_at((int(x), int(y)), col)


def map_func(pt):
    x = pt.real
    y = pt.imag
    return (width/2 + scale*y, height + scale*(x-0.4))
        

pts, ks = gen_mandelbrot_pts(-2.26666,0.4,-2.46666,2.46666,0.0022, max_iter = 250, show_status = True)
cap_pts = gen_triangle_pts(width/2, 0.685*height, 0.225*height, 100000)
star_pts = gen_star_pts(width/2, 0.87*height, 0.065*height, 10000, pi)

plot_mandel_pts(pts, ks, map_func, snow)
plot_pts(cap_pts, lambda pt : (255,0,0))
plot_pts(star_pts)


# displaying the surface and keeping the display running
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()

