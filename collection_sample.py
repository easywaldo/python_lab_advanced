from collections import namedtuple


Point = namedtuple('Point', ['x', 'y'])

p = Point(11, y=22)
print(p)
print(p[0] + p[1])

x, y = p
print(x, y)
print(p.x + p.y)
print(p)