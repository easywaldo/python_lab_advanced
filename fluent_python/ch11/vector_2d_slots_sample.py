from array import array


class Vector2d:
    typecode = 'd'
    
    __match_args__ = ('x', 'y')
    __slots__ = ('__x', '__y')

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)
        
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))
    
    def __iter__(self):
        return (i for i in (self.x, self.y))
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
        


if __name__ == '__main__':
    v1 = Vector2d(1.1, 2.2)
    dumpd = bytes(v1)
    print(dumpd)
    len(dumpd)

    # v1.typecode = 'f' # AttributeError: 'Vector2d' object attribute 'typecode' is read-only
    dumpf = bytes(v1)
    print(dumpf)
    print(len(dumpf))
    print(Vector2d.typecode)
    
    Vector2d.typecode = 'f'
    print(Vector2d.typecode)