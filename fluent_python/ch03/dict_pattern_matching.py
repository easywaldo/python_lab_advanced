def get_creators(record: dict) -> list:
    match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'authors': name}:
            return [name]
        case {'type': 'book'}:
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case {'type': 'movie', 'director': name}:
            return [name]
        case _:
            raise ValueError(f'Invalid record: {record!r}')
        
b1 = dict(
    api=1, 
    authors='Douglas Hosfstadter', 
    type='book', 
    title='Godel, Escher, Bach')

b2 = dict(
    api=2, 
    authors=['easywaldo', 'rosie', 'rucia'], 
    type='book', 
    title='Godel, Escher, Bach')
print(get_creators(b1))
print(get_creators(b2))

from collections import OrderedDict
b3 = OrderedDict(api=2, type='book', title='Python in a Nutshell', authors='Martelli Ravenscrosf Holden'.split())
print(get_creators(b3))

# print(get_creators({'type': 'book', 'pages': 770}))

# print(get_creators('Spam, spam, spam'))

food = dict(category='ice cream', flavor='vanilla', cost=199)
match food:
    case {'category': 'ice cream', **details}:
        print(f'Ice cream details: {details}')

from collections import abc
my_dict = {}
print(isinstance(my_dict, abc.Mapping))
print(isinstance(my_dict, abc.MutableMapping))


tuple_data = (1, 2, (30, 40))
print(hash(tuple_data))
h1 = (1, 2, [30, 40])
# print(hash(h1)) # error - unhashable type: 'list'

tuple_frozen = (1, 2, frozenset([30, 40]))
print(hash(tuple_frozen))


d1 = dict(a=1, b=2)
d2 = dict(a=2, b=4, c=6)
from collections import ChainMap

chain = ChainMap(d1, d2)
print(chain['a'])
print(chain['c'])
chain['c']=-1
print(d1)
print(d2)

d1 = dict(a=1, b=2, c=3, d=4)
d2 = dict(b=20, d=40, e=50)
print(d1.keys() & d2.keys())

s = {'a', 'e', 'i'}
print(d1.keys() & s)

print(d1.keys() | s)


from types import MappingProxyType
d = {1: 'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)

# d_proxy[1] = 'x' # TypeError: 'mappingproxy' object does not support item assignment
d[2] = 'B'
print(d_proxy)
print(d_proxy[2])


from collections import Counter
ct = Counter('abracadabra')
print(ct)

ct.update('aaaazzz')
print(ct)

print(ct.most_common(3))