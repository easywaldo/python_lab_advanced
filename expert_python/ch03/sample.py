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


mylist = [1,2,3,4,5]
print(*mylist)
def display(a, b, c, d, e):
    print(f'a, b, c, d, e are {a, b, c, d, e}')
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

display(*mylist)