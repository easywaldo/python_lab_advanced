from collections import Counter
from collections.abc import Iterable, Hashable
from decimal import Decimal
from fractions import Fraction
from typing import TypeVar

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
print(sorted(l))    # TypeError: '<' not supported between instances of 'object' and 'object'
