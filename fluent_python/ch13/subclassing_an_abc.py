from collections import namedtuple, abc

Card = namedtuple('Card', ['rank', 'suit'])

class FrenchDeck2(abc.MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
    
    def __setitem__(self, position, value):
        self._cards[position] = value
        
    def __delitem__(self, position):
        del self._cards[position]
        
    def insert(self, position, value):
        self._cards.insert(position, value)

french_decks = FrenchDeck2()
for deck in french_decks:
    print(deck)
    
french_decks.insert(5, 'diamond')
print(french_decks[5])


# remove and contains
french_decks.remove('diamond')
print(french_decks.__contains__('diamond'))

# extend
print(len(french_decks))
french_decks.extend(french_decks)
print(len(french_decks))

# pop
print(french_decks.pop(10))

# iter
iter_decks = iter(french_decks)
print(next(iter_decks))
print(next(iter_decks))

# reversed
reversed_decks = reversed(french_decks)
for d in reversed_decks:
    print(d)


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
    
class Fake(Tombola):
    def pick(self):
        return 13

print(Fake)
# f = Fake()

import random

class BingoCage(Tombola):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)
        
    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)
        
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')
    
    def __call__(self):
        self.pick()
    

bingo_cage = BingoCage(['apple', 'android', 'google'])
bingo_cage.load(['microsoft', 'windows'])

print(bingo_cage.pick())
print(bingo_cage.pick())
print(bingo_cage.pick())
print(bingo_cage.pick())
print(bingo_cage.pick())
print(bingo_cage.loaded())