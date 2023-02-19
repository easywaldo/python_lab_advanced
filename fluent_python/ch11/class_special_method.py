from array import array
import math

class Vector2d:
    typecode = 'd'
    
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)
        
    def __iter__(self):
        return (i for i in (self.x, self.y))
    
    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)
    
    def __str__(self):
        return str(tuple(self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))
    
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)
    
    @classmethod
    def frombytes(cls, octets):
        typecode =chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)
    
    def angle(self):
        return math.atan2(self.x, self.y)
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    def __iter__(self):
        return (i for i in (self.x, self.y))
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))
    
    __match_args__ = ('x', 'y')


v1 = Vector2d(3, 4)
print(v1.x, v1.y)

x, y = v1
print(x, y)


print(v1)

v1_clone = eval(repr(v1))
assert v1 == v1_clone

print(v1)

octets = bytes(v1)
print(octets)

print(abs(v1))

print(bool(v1), bool(Vector2d(0, 0)))



class Demo:
    @classmethod
    def klassmeth(*args):
        return args
    
    @staticmethod
    def statmeth(*args):
        return args
    
dk = Demo.klassmeth()
dk_spam = Demo.klassmeth('spam')
ds = Demo.statmeth()
ds1 = Demo.statmeth('spam')

print(dk)
print(dk_spam)
print(ds)
print(ds1)


print(format(42, 'b'))
print(format(2 / 3, '.1%'))

from datetime import datetime
now = datetime.now()
print(format(now, '%H:%M:%S'))
print("It's now {:%I:%M %p}".format(now))


v1 = Vector2d(3, 4)
print(format(v1))
print(format(v1, '.3f'))    # TypeError: non-empty format string passed to object.__format__

v1 = Vector2d(3, 4)
print(format(v1))
print(format(v1, '.2f'))
print(format(v1, '.3e'))


print(format(Vector2d(1, 1), 'p'))
print(format(Vector2d(1, 1), '.3ep'))
print(format(Vector2d(1, 1), '0.5fp'))


print(v1.x, v1.y)
# v1.x = 7    # AttributeError: property 'x' of 'Vector2d' object has no setter


v1 = Vector2d(3, 4)
v2 = Vector2d(3.1, 4.2)
print(hash(v1), hash(v2))


def keyword_pattern_demo(v: Vector2d) -> None:
    match v:
        case Vector2d(0, 0):
            print(f'{v!r} is null')
        case Vector2d(0):
            print(f'{v!r} is vertical')
        case Vector2d(_, 0):
            print(f'{v!r} is horizontal')
        case Vector2d(x, y) if x==y:
            print(f'{v!r} is diagonal')
        case _:
            print(f'{v!r} is awesome')


v1 = Vector2d(3, 4)
print(v1.x, v1.y)
x, y = v1
print(x, y)
print(v1)

v1_clone = eval(repr(v1))
assert v1 == v1_clone

print(v1)

octets = bytes(v1)
print(octets)

print(abs(v1))
print(bool(v1), bool(Vector2d(0, 0)))


v1_clone = Vector2d.frombytes(bytes(v1))
print(v1_clone)
assert v1 == v1_clone

print(format(v1))
print(format(v1, '.2f'))
print(format(v1, '.3e'))

print(Vector2d(0, 0).angle())
print(Vector2d(1, 0).angle())

epsilon = 10**-8
v1 = abs(Vector2d(0, 1).angle() - math.pi/2) 
v2 = abs(Vector2d(1, 1).angle() - math.pi/4)
print(v1)
print(v2)
print(epsilon)
assert v1 > epsilon
assert v2 < epsilon

v1 = format(Vector2d(1, 1), 'p')
v2 = format(Vector2d(1, 1), '.3ep')
v3 = format(Vector2d(1, 1), '0.5fp')
print(v1)
print(v2)
print(v3)



v1 = Vector2d(3, 4)
v2 = Vector2d(3.1, 4.2)
print(v1.x, v1.y)
print(len({v1, v2}))


v1 = Vector2d(3, 4)
print(v1.__dict__)
print(v1._Vector2d__x)


class Pixel:
    __slots__ = ('x', 'y')
    
p = Pixel()
# print(p.__dict__)       # AttributeError: 'Pixel' object has no attribute '__dict__'. Did you mean: '__dir__'?

p.x = 10
p.y = 20
# p.color = 'red' # AttributeError: 'Pixel' object has no attribute 'color'


class OpenPixel(Pixel):
    pass

op = OpenPixel()
print(op.__dict__)

op.x = 8
print(op.__dict__)
print(op.x)
op.color = 'green'

print(op.__dict__)


class ColorPixel(Pixel):
    __slots__ = ('color',)
    
cp = ColorPixel()
# print(cp.__dict__)    # AttributeError: 'ColorPixel' object has no attribute '__dict__'. Did you mean: '__dir__'?

cp.x = 2
cp.color = 'blue'
cp.flavor = 'banana'    # AttributeError: 'ColorPixel' object has no attribute 'flavor'

