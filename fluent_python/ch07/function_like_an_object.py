def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n -1)

print(factorial(42))

print(factorial.__doc__)

print(type(factorial))

fact = factorial
print(fact)

print(fact(5))

map_fact = map(factorial, range(11))
print(map_fact)

print(list(map(factorial, range(11))))

print(fact(10))