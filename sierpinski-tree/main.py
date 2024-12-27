import pygame
from anarchy import *
from utils import *


# pygame initialization
pygame.init()
width = 1850
height = 1000
surf = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sierpinski Tree")
surf.fill((0,0,0))      # black background


# plot points inside pts_list, by lighting up pixels at
# those coordinates. color_func decides the color
def plot_pts(pts_list, color_func = lambda pt : (255,255,255), surface = surf):
    for pt in pts_list:
        pt = (int(pt[0]), height - int(pt[1]))      # integer coordinates and y-coordinate flipping
        surface.set_at(pt, color_func(pt))


# Christmas themed color function - based on red, green and white colors
# chris_col_func = circ_gradient(width/2, height/2 - 100, ((255,50,50), (0,175,255), (255,50,50), (0,200,0)), 300)
chris_col_func = circ_gradient(width/2, height/2 - 100, ((255,50,50), (0,200,0), (255,50,50), (0,175,255)), 300)

# generating the leaves and trunk
leaves_pts = gen_tree_pts(width/2, height/2 - 110, 590, 3, 300000)
trunk_pts = gen_carpet_pts(width/2, height/2 - 400, 240, 240, 100000)

snowflakes = []
snowflakes_colfuncs = []

# snowflakes - vicsek fractals
for i in range(25):
    x = width/2 + random.choice([1, -1])*(0.16*width + random.random()*0.34*width)
    y = 25 + random.random()*(height-50)
    angle = random.random()*2*pi
    size = 15 + 65*random.random()
    initial_col = ratio_div_3d(cyan, blue, 0.5 + 0.5*random.random())
    terminal_col = ratio_div_3d(cyan, blue, 0.1 + 0.4*random.random())
    snowflakes.append(gen_vicsek_pts(x, y, size, angle, 10000))
    snowflakes_colfuncs.append(radial_gradient(x, height - y, (initial_col, terminal_col), 0.5*size))


for snowflake, col_func in zip(snowflakes, snowflakes_colfuncs):
    plot_pts(snowflake, col_func)
    

# plotting leaves and trunk on the surface
plot_pts(trunk_pts, lambda pt : (110,38,14))
plot_pts(leaves_pts, chris_col_func)

# displaying the surface and keeping the display running
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()

