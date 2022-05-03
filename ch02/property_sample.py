# No use property

class SampleA:
    def __init__(self):
        self.x = 0
        self.__y = 99    # private 변수이면 변수명을 변경한다.
        self._z = 0
        
a = SampleA()
a.x = 10


print('Ex2 > x : {}'.format(a.x))
# print('Ex2 > y : {}'.format(a.__y))

print('Ex2 > z : {}'.format(a._z))

print('Ex2 > ', dir(a))


a._SampleA__y = 100 # 수정 가능하지만 권장하지 않는다.
print('Ex2 > y : {}'.format(a._SampleA__y))