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
# print(next(gen))
# print(next(gen))
# print(next(gen))


def vowel(c):
    return c.lower() in 'aeiou'

print(list(filter( vowel, 'Aardvark')))

print(list(itertools.filterfalse(vowel, 'Aardvark')))
print(list(itertools.dropwhile(vowel, 'Aardvark')))
print(list(itertools.takewhile(vowel, 'Aardvark')))
print(list(itertools.compress('Aardvark', (1, 0, 1, 1, 0, 1))))
print(list(itertools.islice('Aardvardk', 4)))
print(list(itertools.islice('Aardvark', 4, 7)))
print(list(itertools.islice('Aardvark', 1, 7, 2)))

sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
print(list(itertools.accumulate(sample)))
print(list(itertools.accumulate(sample, min)))
print(list(itertools.accumulate(sample, max)))
import operator
print(list(itertools.accumulate(sample, operator.mul)))
print(list(itertools.accumulate(range(1, 11), operator.mul)))


print('================================================================')
print(list(enumerate('albatroz', 1)))
print(list(map(operator.mul, range(11), range(11))))
print(list(map(operator.mul, range(11), [2, 4, 8])))
print(list(map(lambda a, b: (a, b), range(11), [2, 4, 8])))
print(list(itertools.starmap(operator.mul, enumerate('albatroz', 1))))

sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
print(list(itertools.starmap(lambda a, b: b / a, enumerate(itertools.accumulate(sample), 1))))


print(all([1, 2, 3]))
print(all([1, 0, 3]))


print(all([]))
print(any([1, 2, 3]))
print(any([1, 0, 3]))
print(any([0, 0.0]))
print(any([]))

g = (n for n in [0, 0.0, 7, 8])
print(any(g))
print(next(g))

