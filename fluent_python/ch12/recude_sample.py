import functools

reduce_sample = functools.reduce(lambda a,b: a*b, range(1,6))
print(reduce_sample)
