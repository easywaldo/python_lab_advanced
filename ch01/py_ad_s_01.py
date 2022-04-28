
"""
Chapter 1
Python variable scope
keyword - scope, global, nonlocal, locals, globals
"""

"""
전역변수는 주로 변하지 않는 고정값에 사용
지역변수 사용이유 : 지역변수는 함수 내에 로직 해결에 주로 사용, 소멸주기 : 함수 실행 해제 시
전역변수를 지역내에서 수정되는 패턴은 권장되지 않는다
"""
    
a = 10 # gloabl variable

def foo():
    # read gloabl variable
    print('Ex1 > ', a)
    
foo()

# read gloabl variable
print('Ex1 > ', a)


# Ex2
b = 20
def bar():
    b = 30
    print('Ex2 > ', b)   # read local variable
bar()

print('Ex2 > ', b)

# Ex3
c = 40

def foobar():
    # c = c + 10
    # c = 10
    # c += 100
    # UnboundLocalError: local variable 'c' referenced before assignment
    print('Ex3 > ', c)

foobar()

print('Ex3 > ', c)


# Ex4

d = 50
def barfoo():
    global d        # 사용을 권장하지 않는다!!
    d = 60
    d += 100
    print('Ex4 ', d)
    
barfoo()


# Ex5
# 클로저 또는 데코레이터 패턴
def outer():
    e = 70
    # UnboundLocalError: local variable 'e' referenced before assignment
    def inner():
        nonlocal e
        e += 10 # e = e + 10
        print('Ex5 > ', e)
    return inner
        

in_test = outer() # 클로저
in_test()
in_test()   # 힙영역에서 해당 변수값에 대한 상태를 저장하고 있다


# Ex 6
def func(var):
    x = 10
    def printer():
        print('Ex6 >', 'Printer func inner')
    print('Func inner', locals())

func('Hi')


# Ex 7
print('Ex7 > ', globals())
test_variable = 100
globals()['test_variable'] = 800    # 내부 원리
print('Ex7 > ', globals())


# Ex 8(지역 -> 전역 변수 생성)
for i in range(1, 10):
    for k in range(1, 10):
        globals()['plus_{}_{}'.format(i, k)] = i + k
print(globals())

for i in range(1, 10):
    for k in range(1, 10):
        globals()['plus_{}X{}'.format(i, k)] = i * k
print(globals())

print('Ex8 >', plus_9X9)