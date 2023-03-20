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

