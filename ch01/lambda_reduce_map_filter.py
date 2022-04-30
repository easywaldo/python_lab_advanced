"""
lambda 장점 : 익명, 힙 영역 사용 즉시 소멸, pythonic???, 파이썬 가비지 컬렉션
일반함수 : 재사용성 위해 메모리 저장
시퀀스형 전처리에 주로 Reduce, Map, Filter 사용
"""

# Ex 1
cul = lambda a, b, c: a * b + c
print('Ex1 >', cul(10, 15, 20))

# Ex 2
digit1 = [x * 10 for x in range(1, 11)]
print('Ex2 > ', digit1)


def ex2_func(x):
    return x ** 2

result = list(map(lambda i: 1 **2, digit1))
print(result)


def also_square(nums):
    def double(x):
        return x ** 2
    return map(double, nums)

print('Ex2 >', list(also_square(digit1)))


# Ex3
digit2 = [1,2,3,4,5,6,7,8,9,10]
result = list(filter(lambda x: x % 2 == 0, digit2))
print('Ex3 > ', result)

def also_evens(nums):
    def is_even(x):
        return x % 2 == 0
    return filter(is_even, nums)

print('Ex3 > ', list(also_evens(digit2)))



# Ex 4
from functools import reduce

digit3 = [x for x in range(1, 101)]
result = reduce(lambda x, y: x + y, digit3)
print('Ex 4 > ' , result)

def also_add(nums):
    def add_plus(x, y):
        return x + y
    return reduce(add_plus, digit3)
print('Ex 4 > ', also_add(digit3))