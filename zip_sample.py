zip_sample = zip(range(3), 'ABC')
print(zip_sample)
print(list(zip_sample))

print(list(zip(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3])))
from itertools import zip_longest
print(list(zip_longest(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3], fillvalue=-1)))

a = [(1,2,3), (4,5,6)]
zip_list = list(zip(*a))
print(zip_list)

b = [(1,2), (3,4), (5,6)]
zip_list = list(zip(*b))
print(zip_list)