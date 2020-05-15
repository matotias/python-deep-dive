# Regular case with tuples
from random import randint, random
from collections import namedtuple


def random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    alpha = round(random(), 2)
    return red, green, blue, alpha


# With a named tuple
Color = namedtuple('Color', 'red green blue alpha')


def random_color_named() -> Color:
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    alpha = round(random(), 2)
    return Color(red, green, blue, alpha)


color = random_color_named()
print(color.red)
print(color.green)
print(color.blue)
print(color.alpha)
