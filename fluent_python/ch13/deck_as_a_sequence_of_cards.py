import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
def set_card(deck, position, card):
    deck._cards[position] = card


french_decks = FrenchDeck()
for deck in french_decks:
    print(deck)

from random import shuffle
deck = FrenchDeck()
# shuffle(deck)   TypeError: 'FrenchDeck' object does not support item assignment

# this is Monky patching
FrenchDeck.__setitem__ = set_card
shuffle(deck)
print(deck[:5])


field_names = 'easywaldo,new york,seoul,L.A'
try:
    field_names = field_names.replace(',', ' ').split()
except AttributeError:
    pass

field_names = tuple(field_names)
if not all(s.isidentifier() for s in field_names):
    raise ValueError('field_names must all be valid identifiers')
print(field_names)