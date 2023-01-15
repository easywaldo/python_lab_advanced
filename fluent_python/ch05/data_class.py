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
# print(dataclass.asdict(coord))


incorrect_coord = CoordinateData(lat=3.12, lon=None) # mypy error


class DemoPlainClass:
    a: int
    b: float = 1.1
    c = 'spam'
    
print(DemoPlainClass.__annotations__)
# print(DemoPlainClass.a) # error
print(DemoPlainClass.b)
print(DemoPlainClass.c)


import typing

class DemoNTClass(typing.NamedTuple):
    a: int
    b: float = 1.1
    c = 'spam'
    
print(DemoNTClass.__annotations__)
print(DemoNTClass.a)
print(DemoNTClass.b)
print(DemoNTClass.__doc__)

nt = DemoNTClass(8)
print(nt.a)
print(nt.b)
print(nt.c)


from dataclasses import dataclass

@dataclass
class DemoDataClass:
    a: int
    b: float = 1.1
    c = 'spam'
    
print(DemoDataClass.__annotations__)
print(DemoDataClass.__doc__)
print(DemoDataClass.b)
print(DemoDataClass.c)


from dataclasses import dataclass, field

@dataclass
class ClubMember:
    name: str
    guests: list[str] = field(default_factory=list)
    athlete: bool = field(default=False, repr=False)
    
cm_1 = ClubMember(name="easywaldo", guests=['alpha', 'bravo'])
print(cm_1)

@dataclass
class HackerClubMember(ClubMember):
    all_handles = set()
    handle: str = ''       

    def __post_init__(self):
        cls = self.__class__
        if self.handle == '':
            self.handle = self.name.split()[0]
        if self.handle in cls.all_handles:
            msg = f'handle {self.handle!r} already exists.'
            raise ValueError(msg)
        cls.all_handles.add(self.handle)
        
print(HackerClubMember.__doc__)

hacker_club_member = HackerClubMember(name='easywaldo', guests=['alpha', 'bravo'])
hacker_club_member = HackerClubMember(name='easywaldo', guests=['a', 'b'])