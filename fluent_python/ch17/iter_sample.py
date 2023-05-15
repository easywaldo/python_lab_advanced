from random import randint

def d6():
    return randint(1, 6)

d6_tier = iter(d6, 1)
for n in d6_tier:
    print(n)