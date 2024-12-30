# Sierpinski Tree

## The fractals involved

The *Sierpinski Tree*, as the name suggests, is largely made of Sierpinksi fractals:
- It's trunk is a Sierpinski carpet, generated using chaos game, with the number of points inside it being
    - `main.py`: 1,00,000
    - `sv-main.py`: 7,50,000
- It's leaves are 3 Sierpinksi triangles, stacked on top of each other, with the number of points in each triangle being
    - `main.py`: 2,00,000
    - `sv-main.py`: 20,00,000
- The snowflakes are all randomly placed, coloured, and oriented. Each one of them is a Vicsek fractal with the number of points in each of them being
    - `main.py`: 10,000
    - `sv-main.py`: 1,00,000

You can find images of each of these fractals in their full glory down below. The points for each of these were generated using the code inside `individual.py`

## File contents

Here's some info on the files and directories

- `sierpinski-tree-4k.png`: The main 4K image that I'm submitting, generated using `sv-main.py`

- `utils.py`:
    A Python module with some useful "utility" functions, among some frequently used constants. This module is used by every other `.py` file

- `anarchy.py`:
    Contains functions that use chaos game to generate points for fractals. These functions are chaos generators, hence the module's name

- `main.py`:
    The main Python file. Running it should open a window of near-HD resolution. The image should be rendered in under 10 seconds.

- `sv-main.py`:
    The main Python file for saving a 4K image. Rendering this image will take a considerable amount of time and the image will be saved in the current working directory

- `individuals`:
    Contains images of the individual fractals used, not meant as submissions but as a showcase of these beauties in their complete glory, unrestricted by the lack of resolution in main image. The code used for generating these images is in the `code` sub-directory.
