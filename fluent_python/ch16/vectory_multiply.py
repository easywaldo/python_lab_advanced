from collections import abc
from array import array
import reprlib


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
        return (len(self) == len(other) and
                all(a == b for a, b in zip(self, other)))
    
    
    

v1 = Vector([1.0, 2.0, 3.0])
print(14 * v1)

print(v1 * True)

from fractions import Fraction
print(v1 * Fraction(1, 3))


print('================================================================')
print(Vector([10, 20, 30]) == Vector([10, 20, 30]))

print('================================================================')
va = Vector([1,2,3])
vz = Vector([5,6,7])
print(va @ vz == 38.0)