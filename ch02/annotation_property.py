"""
keyword @property

사용장점
1. 파이썬 다운 코드
2. 변수제약설정
3. Getter, Setter 효과 동등(코드 일관성)

- 캡슐화-유효성 검사 기능 추가 용이
- 대체 표현(속성노출, 내부의 표혐 숨기기 가능)
- 속성의 수명 및 메모리 관리 용이
"""


class SampleA:
    def __init__(self):
        self.x = 0
        self.__y = 0
        
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError('0보다 큰 값을 입력하세요.')
        self.__y = value
        
    @y.deleter
    def y(self):
        print('deleted')
        del self.__y
        
a = SampleA()




a.x = 1
a.y = 2
print('Ex1 > {}'.format(a.x))
print('Ex1 > {}'.format(a.y))


# deleter
print('Ex1 > ', dir(a))
del a.y
print('called del')
print('Ex1 > ', dir(a))


b = SampleA()

b.x = 1
b.y = 10
b.y = -10