from collections import namedtuple

City = namedtuple('City','name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.name)
print(tokyo.coordinates)
print(tokyo.population)
print(tokyo[:1])