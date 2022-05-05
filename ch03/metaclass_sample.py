"""
1. 메타클래스 동적 생성 중요
2. 동적 생성한 메타클래스 -> 커스텀 메타클래스 생성
3. 의도하는 방향으로 직접 클래스 생성에 관여할 수 있는 큰 장점
"""

# Ex1
# type 동적 클래스 생성 예제


# Name(이름), Bases(상속), Dict(속성, 메서드)

class SampleA():
    pass

s1 = type('Sample1', (), {})

print('Ex1 > ', s1)
print('Ex1 > ', type(s1))
print('Ex1 > ', s1.__base__)
print('Ex1 > ', s1.__dict__)

# 동적 생성 + 상속

class ParentEx1:
    pass

s2 = type(
    'SampleB', 
    (ParentEx1,), 
    dict(name='waldo', age=42)
)

print('Ex2 > ', s2)
print('Ex2 > ', type(s2))
print('Ex2 > ', s2.__base__)
print('Ex2 > ', s2.__dict__)
print('Ex2 > ', s2.name, s2.age)


class SampleC:
    def add(self, a, b):
        return a + b
    
    def mul(self, a, b):
        return a * b

s3 = SampleC()
s4 = type('SampleD', (object, ), dict(attr1=30, attr2=100, add=lambda a, b: a + b, mul=lambda a, b: a * b))
print('Ex3 > ', s3)
print('Ex3 > ', type(s3))
print('Ex3 > ', s3.add(100, 200))
print('Ex3 > ', s3.mul(100, 20))


print('Ex4 > ', s4)
print('Ex4 > ', type(s4))
print('Ex4 > ', s4.add(100, 200))
print('Ex4 > ', s4.mul(100, 20))
