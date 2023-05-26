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

print('================================================================')
gen = itertools.takewhile(lambda n: n < 3, itertools.count(1, .5))
print(list(gen))

def aritprog_gen(begin, step, end=None):
    first = type(begin + step)(begin)
    ap_gen = itertools.count(first, step)
    if end is None:
        return ap_gen
    return itertools.takewhile(lambda n: n < end, ap_gen)

gen = aritprog_gen(2, .5, 5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
