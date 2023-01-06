from functools import reduce
from operator import add


print(reduce(add, range(100)))
print(sum(range(100)))


fruits = ['fig', 'strawberry', 'apple', 'cherry', 'raspberry', 'banana']
result = sorted(fruits, key=lambda word: word[::-1])
print(result)
print(fruits)



import random

class BingoCage:
    
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()


bingo = BingoCage(range(3))
print(bingo.pick())