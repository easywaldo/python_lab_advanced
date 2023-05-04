from collections import Counter


ct = Counter('abracadabra')
print(ct)

ct['r'] = -3
ct['d'] = 0

print(ct)

print(+ct)


ct2 = Counter('american')
print(ct + ct2)

