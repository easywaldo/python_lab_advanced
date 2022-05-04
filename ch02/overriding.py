"""
Chapter 2
Keyword - Overriding, OOP, 다형성
"""

"""
1. 서브클래스(자식)에서 슈퍼(부모)클래스를 호출 후 사용
2. 메서드 재 정의 후 사용 가능
3. 부모클래스의 메서드를 추상화 후 사용가능(구조적 접근)
4. 확장 가능, 다형성(다양한 방식으로 동작)
5. 가독성 증가, 오류가능성 감소, 메서드 이름 절약, 유지보수성 증가 등
"""

class ParentEx1():
    def __init__(self):
        self.value = 50
        
    def get_value(self):
        return self.value
    
class ChildEx1(ParentEx1):
    pass

c1 = ChildEx1()
p1 = ParentEx1()

print('Ex1 > ', c1.get_value())