from functools import reduce
from operator import add


print(reduce(add, range(100)))
print(sum(range(100)))


fruits = ['fig', 'strawberry', 'apple', 'cherry', 'raspberry', 'banana']
result = sorted(fruits, key=lambda word: word[::-1])
print(result)
print(fruits)
