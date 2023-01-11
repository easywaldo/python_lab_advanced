class Coordinate:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        
moscow = Coordinate(55.76, 37.62)
print(moscow)
location = Coordinate(55.76, 37.62)
print(moscow == location)

print((moscow.lat, moscow.lon) == (location.lat, location.lon))

from collections import namedtuple
Coordinate = namedtuple('Coordinate', 'lat lon')
print(issubclass(Coordinate, tuple))
moscow = Coordinate(55.76, 37.617)
print(moscow)
print(moscow == Coordinate(lat=55.76, lon=37.617))
print(Coordinate(lat=55.76, lon=37.617) == Coordinate(lat=55.76, lon=37.617))

import typing
Coordinate = typing.NamedTuple(
    'Coordinate', 
    [('lat', float), ('lon', float)])
print(issubclass(Coordinate, tuple))
print(typing.get_type_hints(Coordinate))