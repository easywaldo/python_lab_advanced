from array import array
import operator
import reprlib
import math

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

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(self._components))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(*self)

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)
    
    def __len__(self):
        return len(self._components)
    
    def __getitem__(self, key):
        if isinstance(key, slice):
            cls = type(self)
            return cls(self._components[key])
        index = operator.index(key)
        return self._components[index]


if __name__ == '__main__':
    vector = Vector([3.1, 4.2])
    print(vector)
    
    v1 = Vector([3, 4, 5])
    print(v1)
    print(v1[0])
    print(v1[-1])
    
    v2 = Vector(range(100))
    print(v2)
    print(v2[1:4])
    
    print('================================================================')
    v7 = Vector(range(7))
    print(v7[-1])
    print(v7[1:4])
    print(v7[-1:])
    print(v7[1,2])  # TypeError: 'tuple' object cannot be interpreted as an integer
    
    