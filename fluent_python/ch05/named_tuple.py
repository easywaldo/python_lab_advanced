from collections import namedtuple


Coordinate = namedtuple('Coordinate', 'lat lon reference', defaults=['WGS84'])
print(Coordinate._field_defaults)