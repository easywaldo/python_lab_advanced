def gen_123():
    yield 1
    yield 2
    yield 3
    
print(gen_123)

for i in gen_123():
    print(i)
    
g = gen_123()
print(next(g))
print(next(g))
print(next(g))
# print(next(g))


def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')
    
for c in gen_AB():
    print('--->', c)
    
    
import itertools
gen = itertools.count(1, .5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

