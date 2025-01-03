"""Some utility functions"""

import math
import random

# some useful constants
pi = math.pi
# RGB values for some frequently used colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
cyan = (0, 255, 255)


# the signum function, implemented using
# short-circuiting of the boolean operators
def sgn(x):
    return (x != 0 and int(x/abs(x))) or 0


# "extended" arctan function :
# gives the angle from (a, b) to (c, d) in the range [0, 2pi)
# LaTeX verison: https://imgur.com/a/Q30wEVR
# (I came up with this myself)
def eatan(a, b, c, d):
    # if a = c, returns pi/2 or 3pi/2, based on b and d
    if a == c:
        return pi/2*(2 + sgn(b-d))
    # else, employs the formula from the image
    return math.atan((b-d)/(a-c)) + pi*sgn(1 + sgn(a-c)) + 2*pi*sgn(sgn(a-c) - 1)*sgn(sgn(d-b) - 1)


# gives the abscissa of the point that divides the
# segment from (k1, 0) to (k2, 0) in the ratio r : (1-r)
def ratio_div(k1, k2, r):
    return ((1-r)*k1 + r*k2)


# internal division in the ratio r : (1-r) for two 3-tuples
# (mostly used here to help make color gradients)
def ratio_div_3d(t1, t2, r):
    if r <= 0:
        return t1
    elif r >= 1:
        return t2
    return (ratio_div(t1[0], t2[0], r), ratio_div(t1[1], t2[1], r), ratio_div(t1[2], t2[2], r))


# dividing two 2-tuples in the ratio r : 1-r
def ratio_div_2d(p1, p2, r):
    return (ratio_div(p1[0], p2[0], r), ratio_div(p1[1], p2[1], r))


# mid-point of two 2-tuples
def midpoint_2d(p1, p2):
    return ratio_div_2d(p1, p2, 0.5)


# generates a 'color function' that will correspond to a 'circular gradient',
# which is described below
#
# for some point (x, y), let r be it's distance from (x0, y0) and theta
#       be the angle it makes with y = y0, in the range [0, 2pi), then the
#       colors depend on theta like so:
#
#             0 < theta < 2pi/n -> linear gradient b/n cols[0] and cols[1]
#         2pi/n < theta < 4pi/n -> linear gradient b/n cols[1] and cols[2]
#                     ...       ->                ...
#     (n-1)*2pi/n < theta < 2pi -> linear gradient b/n cols[-1] and cols[0]
#
# let the color given by the above conditions be denoted by c. Then the final
#       color varies linearly from white to c, with the factor r/r_max, i.e.
#                   (1-r/r_max)*white + r/r_max*c
def circ_gradient(x0, y0, cols, r_max, offset=0):
    def func(pt):
        ncols = len(cols)       # number of colors
        phi = 2*pi/ncols        # angle between two successive colors
        x = pt[0]
        y = pt[1]
        r = (x**2 + y**2)**0.5
        theta = (eatan(x0, y0, x, y) - offset) % (2*pi)
        lval = int(theta/phi)
        col = ratio_div_3d(cols[lval], cols[(lval+1) % ncols], theta/phi - math.floor(theta/phi))
        return ratio_div_3d((255, 255, 255), col, r/r_max)
    return func


# generates a color function that corresponds to a radial gradient centered
# at (x0, y0), from cols[0] to cols[1], where cols[1] is fully attained at r_max
def radial_gradient(x0, y0, cols, r_max):
    def func(pt):
        col1, col2 = cols
        x = pt[0]
        y = pt[1]
        r = ((x-x0)**2 + (y-y0)**2)**0.5
        return ratio_div_3d(col1, col2, r/r_max)
    return func


# random point inside a rectangle
# (x, y) -> bottom left corner
# l x w  -> dimensions
def rand_rect(x, y, l, w):
    return (x + random.random()*l, y + random.random()*w)


# random point inside a circle
# (x, y) -> centre
# r      -> radius
def rand_circ(x, y, r):
    rand_r = random.random()*r
    rand_theta = random.random()*2*pi
    return (x + rand_r*math.cos(rand_theta), y + rand_r*math.sin(rand_theta))


# evaluates the point at a distance of `l` units from
# pt, making an angle `a` with the line `y = pt[1]`
def polar_sum(pt, l, a):
    return (pt[0] + l*math.cos(a), pt[1] + l*math.sin(a))

