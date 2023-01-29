from collections.abc import Iterable
from decimal import Decimal
from fractions import Fraction
from typing import TypeVar

NumberT = TypeVar('NumberT', float, Decimal, Fraction, str)

def mode(data: Iterable[NumberT]) -> NumberT:
    pass


from statistics import mode
mode_list = mode(["red", "green", "blue", "yellow", "red", "green", "blue", "yellow", "red", "red"])
print(mode_list)