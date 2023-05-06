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
    

v1 = Vector([1.0, 2.0, 3.0])
print(14 * v1)

print(v1 * True)

from fractions import Fraction
print(v1 * Fraction(1, 3))