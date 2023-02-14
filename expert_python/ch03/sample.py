dict1 = {
    'a': 1
}
dict2 = {
    'b': 2
}

print('================================')
print(dict1 | dict2)

mydict = {'a': 1}
mydict |= {'a': 3, 'b': 4}
print(mydict)

other_dict = {'c': 99, 'd': 88}
print({**mydict, **other_dict})
