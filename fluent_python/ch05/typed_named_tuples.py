import typing

class Coordinate(typing.NamedTuple):
    lat: float
    lon: float
    reference: str = 'WSG84'
    
trash = Coordinate('Ni!', None)
print(trash)