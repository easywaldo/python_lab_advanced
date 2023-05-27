import itertools


print(list(itertools.groupby('LLLLAAGGG')))

for char, group in itertools.groupby('LLLLAAAGG'):
    print(char, '->', list(group))

animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear', 'bat', 'dolphin', 'shark', 'lion']
animals.sort(key=len)

print(animals)