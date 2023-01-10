s = 'café'
print(len(s))

b = s.encode('utf8')
print(b)

print(len(b))

print(b.decode('utf8'))


cafe = bytes('café', encoding='utf_8')
print(cafe)

print(cafe[0])
print(cafe[:1])

cafe_arr = bytearray(cafe)
print(cafe_arr)

print(cafe_arr[-1:])


print(bytes.fromhex('31 4B CE A9'))
import array
numbers = array.array('h', [-2, -1, 0, 1, 2])
octets = bytes(numbers)
print(octets)


for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec, 'El Niño'.encode(codec), sep='\t')
    
    
city = 'São Paulo'
print(city.encode('utf_8'))
print(city.encode('utf_16'))
print(city.encode('iso8859_1'))
# print(city.encode('cp437')) # error


print(city.encode('cp437', errors='ignore'))
print(city.encode('cp437', errors='replace'))
print(city.encode('cp437', errors='xmlcharrefreplace'))


octets = b'Montr\xe9al'
print(octets.decode('cp1252'))
print(octets.decode('iso8859_7'))
print(octets.decode('koi8_r'))
# print(octets.decode('utf_8')) # error

print(octets.decode('utf_8', errors='replace'))