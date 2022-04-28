
"""
Chapter 1
Python variable scope
keyword - scope, global, nonlocal, locals, globals
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