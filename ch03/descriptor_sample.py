"""
python advanced - descriptor
keyword - descriptor, set, get, del, property


1. 객체에서 서로 다른 객체를 속성값으로 가지는 것
2. Read, Write, Delete 등을 미리 정의 가능
3. data description(set, del), non-date descriptor(get)
4. 읽기전용 객체생성 장점, 클래스를 의도하는 방법으로 생성 가능

"""


class DescriptorEx1(object):
    def __init__(self, name='Default Name'):
        self.name = name
        
    def __get__(self, obj, obj_type):
        return 'Get method called. -> self : {}, obj : {}, obj_type : {}, name : {}'.format(self, obj, obj_type, self.name)
    
    def __set__(self, obj, name):
        print('Set method called')
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError('Name should be string')
        
    def __delete__(self, obj):
        print('Delete method called')
        self.name = None
        
class Sample1(object):
    name = DescriptorEx1()
    
s1 = Sample1()
print(s1.name)

s1.name = 'descriptor test1'

# attr 확인
# __get__ 호출
print('Ex1 > ', s1.name)


# __delete__ 호출
del s1.name

# 재확인
# __get__ 호출
print('Ex1 > ', s1.name)


# Ex2
# property 클래스 사용 descriptor 직접 구현
# class property(fget=None, fset=None, doc=None)

class DescriptorEx2(object):
    def __init__(self, value):
        self._name = value
        
    def getValue(self):
        return 'Get method called. =>> self : {}, name : {}'.format(self, self._name)
    
    def setValue(self, value):
        print('Set method called')
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError('Name should be string')
    
    def delValue(self):
        print('Delete method called')
        self._name = None
        
    name = property(getValue, setValue, delValue, 'Property method example')


s2 = DescriptorEx2('Descriptor Test2')

# 최초 값 확인
print('Ex2 > ', s2.name)

# setValue 호출
s2.name = 'Descriptor test2 method'

print('Ex2 > ', s2.name)

# delValue 호출
del s2.name

# 재확인
print('Ex2 > ', s2.name)

print(DescriptorEx2.name.__doc__)

s2.name = 999


