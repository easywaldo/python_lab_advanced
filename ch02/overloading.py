"""
메서드 오버로딩 효과

1. 동일 메서드 재정의
2. 네이밍 가능 에측
3. 코드절약, 가독성 향상
4. 메서드 파라미터 기반 호출방식

keyword >> multiple dispatch
"""

# Ex1
# 동일 이름 메서드 사용예제
# 동적타입검사 >>> 런타임에 실행(타임에러가 실행시에 발견)

class SampleA():
    def add(self, x, y):
        return x + y
    
    def add(self, x, y, z):
        return x + y + z
    
a = SampleA()
print('Ex1 >', a.add(2,3,10))

# 모든 속성 개체 확인
print('Ex1 >', dir(a))

class SampleB():
    def add(self, datatype, *args):
        if (datatype == 'int'):
            return sum(args)
        if (datatype == 'str'):
            return ''.join([x for x in args])
        
b = SampleB()

# 숫자연산
print('Ex2 >', b.add('int', 10, 9))

# 문자열연산
print('Ex2 >', b.add('str', 'hi','python'))


from multipledispatch import dispatch

class SampleC():
    
    @dispatch(int, int)
    def product(x, y):
        return x * y

    @dispatch(int, int, int)
    def product(x, y, z):
        return x * y * z
    
    @dispatch(float, float, float)
    def product(x, y, z):
        return x * y * z
    
c = SampleC()

print('Ex3 >', c.product(5,6))
print('Ex3 >', c.product(5,6,7))
print('Ex3 >', c.product(5.0,6.0,7.0))
