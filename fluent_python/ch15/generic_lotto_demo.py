import random

from collections.abc import Iterable
from typing import TypeVar, Generic


T = TypeVar('T')

import abc
class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable):
        """Add items from an iterable"""
        
    @abc.abstractmethod
    def pick(self):
        """Remove item at random, returning it."""
        
    def loaded(self):
        """Return True if there is at least one item"""
        return bool(self.inspect())
    
    def inspect(self):
        """Return a sorted tuple with the items currently inside."""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(items)


class LottoBlower(Tombola, Generic[T]):

    def __init__(self, items: Iterable[T]) -> None:
        self._balls = list[T](items)

    def load(self, items: Iterable[T]) -> None:
        self._balls.extend(items)

    def pick(self) -> T:
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty LottoBlower')
        return self._balls.pop(position)

    def loaded(self) -> bool:
        return bool(self._balls)

    def inspect(self) -> tuple[T, ...]:
        return tuple(self._balls)
    

machine = LottoBlower[int](range(1, 11))
first = machine.pick()
remain = machine.inspect()


machine = LottoBlower[int]([1, .2])
machine = LottoBlower[int](range(1, 11))
machine.load('ABC')