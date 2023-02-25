from typing import Optional
from pytest import mark

def show_count(count: int, singular: str, plural: Optional[str] = None) -> str:
    if count == 1:
        return f'1 {singular}'
    count_str = str(count) if count else 'no'
    if not plural:
        plural = singular + 's'
    return f'{count_str} {plural}'

@mark.parametrize('qty, expected', [
    (1, '1 part'),
    (2, '2 parts'),
])
def test_show_count(qty, expected):
    got = show_count(qty, 'part')
    assert got == expected

def test_show_count_zero():
    got = show_count(0, 'part')
    assert got == 'no parts'
    
def test_irregular() -> None:
    got = show_count(2, 'child', 'children')
    assert got == '2 children'
<<<<<<< HEAD
=======
    
from collections import abc

def double(x: abc.Sequence):
    """
    Unsupported operand types for * ("Sequence[Any]" and "int")
    """
    return x * 2

def test_double_seq():
    seq_num = yield [n for n in range(1,5)]
    assert double(seq_num) == list(2,4,6,8,10)
    assert double("hello world") == "hello worldhello world"


class Bird:
    pass

class Duck(Bird):
    def quack(self):
        print('Quack')

def alert(birdie):
    birdie.quack()
    
def alert_duck(birdie: Duck) -> None:
    birdie.quack()
    
def alert_bird(birdie: Bird) -> None:
    birdie.quack()  # error: "Bird" has no attribute "quack"
<<<<<<< HEAD
>>>>>>> 0c92e51e789137a3b270b0a57ad258664f517da9
=======

from typing import NamedTuple

from geolib import geohash as gh

PERCISON = 9

class Coordinate(NamedTuple):
    lat: float
    lon: float

def geohash(lat_lon: Coordinate) -> str:
    return gh.encode(*lat_lon, PERCISON)

def display(lat_lon: tuple[float, float]) -> str:
    lat, lon = lat_lon
    ns = 'N' if lat >= 0 else 'S'
    ew = 'E' if lon >= 0 else 'W'
    return f'{abs(lat):0.1f}°{ns}, {abs(lon):0.1f}°{ew}'


coordinate = Coordinate(lat=20.34, lon=31.48)
print(coordinate._asdict())

print(display(coordinate))


from typing import TypeAlias

FromTo: TypeAlias = tuple[str, str]


from collections.abc import Sequence
from random import shuffle
from typing import TypeVar

T = TypeVar('T')

def sample(population: Sequence[T], size: int) -> list[T]:
    if size < 1:
        raise ValueError('size must be >= 1')
    result = list(population)
    shuffle(result)
    return result[:size]

result = sample(["alpha", "beta", "bravo", "charly"], 4)
print(result)
>>>>>>> bf08e3ca9a388b24b3f21d6176583a0f6cc4ba61
