"""main.py
Running this should open a window in near-HD resolution with the generated image.
Run sv-main.py to generate and save a 4K image (takes a lot of time to render)
"""

import pygame
from anarchy import *


# pygame initialization
pygame.init()
# the screen's resolution
width = 1850
height = 1000
surf = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sierpinski Tree")       # the window's title
surf.fill((0,0,0))          # a black background


# plot points inside pts_list, by lighting up pixels at
# those coordinates. color_func decides the color based on
# the points' coordinates
def plot_pts(pts_list, color_func = lambda pt : (255,255,255), surface = surf):
    for pt in pts_list:
        pt = (int(pt[0]), height - int(pt[1]))      # integer coordinates and y-coordinate flipping
        surface.set_at(pt, color_func(pt))


# a Christmas-themed color function used for the tree
chris_col_func = circ_gradient(width/2, height/2 - 100, ((255,50,50), (0,200,0), (255,50,50), (0,175,255)), 300)


# generating the leaves and trunk
leaves_pts = gen_tree_pts(width/2, height/2 - 110, 590, 3, 200000)
trunk_pts = gen_carpet_pts(width/2, height/2 - 400, 240, 240, 100000)


# lists to store the snowflakes and their color functions
snowflakes = []
snowflakes_colfuncs = []


# generating 25 snowflakes with randomized parameters such as their
# position, size, colors and orientation; and storing them in the lists above
for i in range(25):
    # randomized position such that they (usually) don't collide with the tree
    x = width/2 + random.choice([1, -1])*(0.16*width + random.random()*0.34*width)
    y = 25 + random.random()*(height-50)
    
    angle = random.random()*2*pi        # randomized angle for orientation
    size = 15 + 65*random.random()      # randomized size
    
    # parameters to get a randomized color function
    initial_col = ratio_div_3d(cyan, blue, 0.5 + 0.5*random.random())
    terminal_col = ratio_div_3d(cyan, blue, 0.1 + 0.4*random.random())
    
    # updating the lists with the generated snowflakes
    snowflakes.append(gen_vicsek_pts(x, y, size, angle, 10000))
    snowflakes_colfuncs.append(radial_gradient(x, height - y, (initial_col, terminal_col), 0.5*size))


# plotting the snowflakes
for snowflake, col_func in zip(snowflakes, snowflakes_colfuncs):
    plot_pts(snowflake, col_func, surface = surf)
    
# plotting the leaves and the trunk
plot_pts(trunk_pts, lambda pt : (110,38,14), surface = surf)
plot_pts(leaves_pts, chris_col_func, surface = surf)


# displaying the surface and keeping the display running
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()

