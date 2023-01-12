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

Coordinate = typing.NamedTuple('Coordinate',lat=float,lon=float)
print(issubclass(Coordinate, tuple))
print(typing.get_type_hints(Coordinate))

from typing import NamedTuple

class Coordinate(NamedTuple):
    lat: float
    lon: float
    
    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'
    
# print(issubclass(Coordinate, typing.NamedTuple)) # error
print(issubclass(Coordinate, tuple))

from dataclasses import dataclass

@dataclass(frozen=True)
class CoordinateData:
    lat: float
    lon: float
    
    def __str__(self) -> str:
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'
    
coord = CoordinateData(lat=3.12, lon=12.66)
print(coord.lat)
print(coord.lon)
print(coord.__annotations__)
print(dataclasses.asdict(coord))
