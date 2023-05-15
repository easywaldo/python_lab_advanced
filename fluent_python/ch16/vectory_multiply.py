from collections import abc
from array import array
import reprlib


class Vector2d:
    typecode = 'd'
    
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)
        
    def __iter__(self):
        return (i for i in (self.__x, self.__y))
    
    def __len__(self):
        return int(self.__y - self.__x)
    
    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)
    
    def __eq__(self, other):
        if (isinstance(other, tuple)):
            return False
        return tuple(self) == tuple(other)


class Vector:
    typecode = 'd'
    
    def __init__(self, components):
        self._components = array(self.typecode, components)
        
    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return f'Vector({components})'
        
    def __mul__(self, scalar):
        try:
            factor = float(scalar)
        except TypeError:
            return NotImplemented
        return Vector(n * factor for n in self)
    
    def __rmul__(self, scalar):
        return self * scalar
    
    def __matmul__(self, other):
        if (isinstance(other, abc.Sized) and
            isinstance(other, abc.Iterable)):
            if len(self) == len(other):
                return sum(a * b for a, b in zip(self, other))
            else:
                raise ValueError('@ requires vectors of equal length.')
        else:
            return NotImplemented
    
    def __rmatmul__(self, other):
        return self @ other
    
    def __len__(self):
        return len(self._components)
    
    def __eq__(self, other):
        if isinstance(other, Vector):
            return (len(self) == len(other) and
                    all(a == b for a, b in zip(self, other)))
        else:
            return NotImplemented
        
    def __ne__(self, other):
        eq_result = self == other
        if eq_result is NotImplemented:
            return NotImplemented
        else:
            return not eq_result
    
    
    

v1 = Vector([1.0, 2.0, 3.0])
print(14 * v1)

print(v1 * True)

from fractions import Fraction
print(v1 * Fraction(1, 3))


print('================================================================')
print(Vector([10, 20, 30]) == Vector([10, 20, 30]))
print(Vector([1.0, 2.0, 3.0]) == (1, 2, 3))

print('================================================================')
va = Vector([1,2,3])
vz = Vector([5,6,7])
print(va @ vz == 38.0)


va = Vector([1.0, 2.0, 3.0])
vb = Vector(range(1, 4))

print(va == vb)

vc = Vector([1, 2])

v2d = Vector2d(1, 2)
print(vc == v2d)

t3 = (1, 2, 3)
print(va == t3) # compare Vector with tuple


print('================================================================')
print(va != vb)
print(vc != v2d)
print(va != (1,2,3))

