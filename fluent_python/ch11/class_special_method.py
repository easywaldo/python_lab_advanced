from array import array
import math

class Vector2d:
    typecode = 'd'
    
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        
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
v1.x = 7    # AttributeError: property 'x' of 'Vector2d' object has no setter
