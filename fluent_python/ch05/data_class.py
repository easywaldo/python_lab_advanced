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
from datetime import date
from enum import Enum, auto
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

from typing import ClassVar, NamedTuple, Optional

class Coordinate(NamedTuple):
    lat: float
    lon: float
    
    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'
    
# print(issubclass(Coordinate, typing.NamedTuple)) # error
print(issubclass(Coordinate, tuple))

from dataclasses import dataclass, fields

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
# hacker_club_member = HackerClubMember(name='easywaldo', guests=['a', 'b']) # raise error 


class ResourceType(Enum):
    BOOK = auto()
    EBOOK = auto()
    VIEDO = auto()
    
@dataclass
class Resource:
    """
    Media resource description
    """
    identifier: str
    title: str = '<untiled>'
    creators: list[str] = field(default_factory=list)
    date: Optional[date] = None
    type: ResourceType = ResourceType.BOOK
    description: str = ''
    language: str = ''
    subjects: list[str] = field(default_factory=list)
    
    def __repr__(self):
        cls = self.__class__
        cls_name = cls.__name__
        indent = ' ' * 4
        res = [f'{cls_name}(']
        for f in fields(cls):
            value = getattr(self, f.name)
            res.append(f'{indent}{f.name} = {value!r},')

        res.append(')')
        return '\n'.join(res)
    
    
description = 'Improving the design of existing code'
book = Resource(
    '978-0-13-475759-9', 
    'Refactoring, 2nd Edition', 
    ['Martin Fowler', 'Kent Beck'], 
    date(2018, 11, 19), 
    ResourceType.BOOK, 
    description, 
    'EN', 
    ['computer programming', 'OOP'])

print(book)


class City(typing.NamedTuple):
    continent: str
    name: str
    country: str
    

cities = [
    City('Asia', 'Tokyo', 'JP'),
    City('Asia', 'Delhi', 'IN'),
    City('North America', 'Mexico City', 'MX'),
    City('North America', 'New York', 'US'),
    City('South America', 'São Paulo', 'BR'),
]
    
def match_asian_cities():
    results = []
    for city in cities:
        match city:
            case City(continent='Asia'):
                results.append(city)
    return results

def match_asian_countries():
    results = []
    for city in cities:
        match city:
            case City(continent='Asia', country=cc):
                results.append(cc)
    return results

def match_asian_cities_pos():
    results = []
    for city in cities:
        match city:
            case City('Asia'):
                results.append(city)
    return results

print(City.__match_args__)
print(match_asian_cities())
print(match_asian_countries())
print(match_asian_cities_pos())

@dataclass
class Spam:
    repeat: ClassVar[int] = 99
    
spam_inst = Spam()
Spam.repeat = 100
print(spam_inst.repeat)

@dataclass
class Hamber:
    cost = 100
    
hamber = Hamber()
Hamber.cost = 1000
print(hamber.cost)