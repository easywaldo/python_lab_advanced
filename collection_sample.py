from collections import namedtuple


Point = namedtuple('Point', ['x', 'y'])

p = Point(11, y=22)
print(p)
print(p[0] + p[1])

x, y = p
print(x, y)
print(p.x + p.y)
print(p)

from collections import deque

d = deque('ghi')
for elem in d:
    print(elem.upper())

d.append('j')
d.appendleft('f')
print(d)

d.pop()
d.popleft()
print(list(d))
print(d[0])
print(d[-1])

print(list(reversed(d)))
print('h' in d)
d.extend('jkl')
print(d)
d.rotate(1)
print(d)
d.rotate(-1)
print(d)

print(reversed(d))
d.clear()
# d.pop() # IndexError: pop from an empty deque
d.extendleft('abc')
print(d)


print('================================================================')
from collections import defaultdict
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
sorted_dict = sorted(d.items())
print(sorted_dict)
print(type(sorted_dict))
print(sorted_dict[1])
print(d['yellow'])


print('================================================================')
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(dict)
for k, v in s:
    d[k] = v
sorted_dict = sorted(d.items())
print(sorted_dict)
print(type(sorted_dict))
print(d)
print(d['blue'])


d = {}
for k, v in s:
    d.setdefault(k, []).append(v)
result = sorted(d.items())
print(result)
