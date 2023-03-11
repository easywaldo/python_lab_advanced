from array import array


class Vector:
    # many lines omitted
    # ...
    
    typecode = 'd'
    
    def __init__(self, components):
        self._components = array(self.typecode, components)
        
    def __iter__(self):
        return iter(self._components)

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        return self._components[index]
    
v1 = Vector([3,4,5])
print(len(v1))
print(v1[0], v1[-1])

v7 = Vector(range(7))
print(v7)
print(v7[1:4])
