from first import first
result = first([0, False, None, [], (), 42])

print(result)

print(first([-1, 0, 1, 2]))
print(first([-1, 0, 1, 2, 3, 4, 5], key=lambda x: x > 0))


import operator
def greater_than_five(number):
    return number > 5

print(first([-1, 0, 2, 4, 5, 10, 18], key=greater_than_five))
