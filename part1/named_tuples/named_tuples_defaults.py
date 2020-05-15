from collections import namedtuple

# Docstrings
Point2D = namedtuple('Point2D', ['x', 'y'])

print(Point2D.__doc__)
print(Point2D.x.__doc__)
print(Point2D.y.__doc__)
help(Point2D)

Point2D.__doc__ = '2D point'
Point2D.x.__doc__ = 'x coordinate'
Point2D.y.__doc__ = 'y coordinate'

# Prototype
Vector2D = namedtuple('Vector2D', 'x1 y1 x2 y2 origin_x origin_y')
vector_zero = Vector2D(0, 0, 0, 0, 0, 0)
v = vector_zero._replace(x1=10, y1=10, x2=20, y2=20)

# Defaults
Vector2D.__new__.__defaults__ = (0, 0)
v2 = Vector2D(10, 10, 20, 20)


