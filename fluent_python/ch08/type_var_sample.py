from collections import Counter
from collections.abc import Iterable, Hashable
from decimal import Decimal
from fractions import Fraction

from typing import Optional, TypeVar

NumberT = TypeVar('NumberT', float, Decimal, Fraction, str)

def mode(data: Iterable[NumberT]) -> NumberT:
    print('called mode number_t')
    return 100


# from statistics import mode
mode_list = mode(["red", "green", "blue", "yellow", "red", "green", "blue", "yellow", "red", "red"])
print(mode_list)


def mode(data: Iterable[Hashable]) -> Hashable:
    print('called mode hashtable')
    pairs = Counter(data).most_common(1)
    if len(pairs) == 0:
        raise ValueError('no mode for empty data')
    return pairs[0][0]

h_t = list([hash("easywaldo"), hash("alpha"), hash("bravo"), hash("alpha"), hash("alpha"), hash("easywaldo")])
print(mode(h_t))


T = TypeVar('T', int, float, complex)
def top(series: Iterable[T], length: int) -> list[T]:
    ordered = sorted(series, reverse=True)
    return ordered[:length]

number_top_list = top([4,1,5,2,6,7,3], 3)
print(number_top_list)

l = 'mango pear apple kiwi banana'.split()
print(top(l, 3))

l2 = [(len(s), s) for s in l]
print(l2)
print(top(l2, 3))

l = [object() for _ in range(4)]
print(l)
# print(sorted(l))    # TypeError: '<' not supported between instances of 'object' and 'object'


class Spam:
    def __init__(self, n): self.n = n
    def __lt__(self, other): return self.n < other.n
    def __repr__(self) -> str: return f'Spam({self.n})'

l = [Spam(n) for n in range(5, 0, -1)]
print(l)
print(sorted(l))

from typing import Protocol, Any

class SupportsLessThan(Protocol):
    def __init__(self, n): 
        self.n = n
    def __lt__(self, other:Any) -> bool:
        print('called... LT')
        return self.n < other.n
    def __repr__(self) -> str: return f'Spam({self.n})'
    
LT = TypeVar('LT', bound=SupportsLessThan)
def top(series: Iterable[LT], length: int) -> list[LT]:
    ordered = sorted(series, reverse=True)
    return ordered[:length]

from collections.abc import Iterator
from random import randrange
fruit = 'mango pear apple kiwi banana hello'.split()
series: Iterator[tuple[int, str]] = ((len(s), s) for s in fruit)
length = 3
expected = [(6, 'banana'), (5, 'mango'), (5, 'hello')]
result = top(series, length)
assert result == expected
print(result)

l = [SupportsLessThan(randrange(1, 1000)) for _ in range(1,10)]
print(sorted(l, reverse=True))
print(top(l, 3))

from collections.abc import Callable

def update(probe: Callable[[], float],
           display: Callable[[float], None]) -> None:
    temperature = probe()
    display(temperature)
    
def probe_ok() -> int:
    return 42

def display_wrong(temperature: int) -> None:
    print(hex(temperature))

update(probe_ok, display_wrong) # Argument 2 to "update" has incompatible type "Callable[[int], None]"; expected "Callable[[float], None]"

def display_ok(temperature: complex) -> None:
    print(temperature)

update(probe_ok, display_ok)


def tag(
    name: str,
    /,
    *content: str,
    class_: Optional[str] = None,
    **attrs: str,
) -> str:
    return f"{name} {content} {class_} {attrs}"

print(tag("easywaldo", content="hello world", class_="alhpa", grade="A", type="SUPER"))