charles = {'name': 'Charles L. Doggson', 'born': 1832}
lewis = charles
print(lewis is charles)

print(id(charles), id(lewis))

lewis['balance'] = 950
print(charles)
print(lewis)

alex = {'name': 'Charles L. Doggson', 'born': 1832, 'balance': 950}
print(alex == charles)

print(alex is not charles)

t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])
print(t1 == t2)

print(id(t1[-1]))

t1[-1].append(99)
print(t1)

print(id(t1[-1]))
print(t1 == t2)



l1 = [3, [44, 55], (7, 8, 9)]
l2 = list(l1)

print(l2)

print(l2 == l1)

print(l2 is l1)


l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1)   # 3개의 요소로 할당
l1.append(100)  # 4개의 요소로 확장
l1[1].remove(55)    # 55 삭제

print('l1:', l1)
print('l2:', l2)
l2[1] += [33, 22]   # 두번째 요소의 33, 22 추가 -->> list 는 mutable object
l2[2] += (10, 11)   # 세번째 요소에 += 튜플연산자 로 인한 새로운 튜플이 만들어진다. => l1 l2 의 세번째 요소는 달라지게 된다

print('l1:', l1)
print('l2:', l2)


class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)
        
    def pick(self, name):
        self.passengers.append(name)
    
    def drop(self, name):
        self.passengers.remove(name)
        
import copy
bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)
print(id(bus1), id(bus2), id(bus3))

bus1.drop('Bill')
print(bus2.passengers)

print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))
print(bus3.passengers)

a = [10, 20]
b = [a, 30]
a.append(b)
print(a)

c = copy.deepcopy(a)
print(c)


def f(a, b):
    a += b
    return a

x = 1
y = 2
print(f(x, y))

print(x, y)

a = [1, 2]
b = [3, 4]
print(f(a, b))

print(a, b)
t = (10, 20)
u = (30, 40)
print(f(t, u))

print(t, u)


class HauntedBus:
    """
    Haunted Bus
    """
    
    def __init__(self, passengers=[]):
        self.passengers = passengers
    
    def pick(self, name):
        self.passengers.append(name)
        
    def drop(self, name):
        self.passengers.remove(name)
        

bus1 = HauntedBus(["Alice", "Bill"])
print(bus1)

bus1.pick('Charlie')     
bus1.drop('Alice')

print(bus1.passengers)
   
   
bus2 = HauntedBus()
bus2.pick('Carrie')
print(bus2.passengers)


bus3 = HauntedBus()
print(bus3.passengers)


bus3.pick('Dave')
print(bus2.passengers)


print(bus2.passengers is bus3.passengers)
print(bus1.passengers)

print(bus1.passengers is bus2.passengers)


print(dir(HauntedBus.__init__))
print(HauntedBus.__init__.__defaults__)
print(HauntedBus.__init__.__defaults__[0] is bus2.passengers)


class TwilightBus:
    """A bus model that makes passengers vanish"""

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers) # list 로 새로이 만들지 않고 passengers 를 객체에서 변수 참조하게 된다면.. pick 과 drop 에 의해 파라미터가 수정될 수 있음

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

# Passengers disappear when dropped by a TwilightBus
# 리스트로 전달한 파라미터들은 객체의 행동에 의하여 사라져 버렸다. 
# Principle of least astonishment - 놀람 최소화 원칙에 위배되었다고도 할 수 있다

basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
bus = TwilightBus(basketball_team)
bus.drop('Tina')
bus.drop('Pat')
print(basketball_team)


a = [1, 2]
b = a
del a
print(b)

b = [3]
print(b)
# print(a) # error raised


import weakref

s1 = {1, 2, 3,}
s2 = s1

def bye():
    print("... like tears in the rain")

ender = weakref.finalize(s1, bye)
print(ender.alive)  # True  - s1 과 s2 가 모두 {1,2,3} 에 대한 참조를 하고 있음

del s1  # print bye message
print(ender.alive)  # True - s2

s2 = 'spam'
print(ender.alive) # False - 이미 s2 에 대한 참조값이 변경이 되었으므로 {1,2,3} 에 대한 참조 변수가 없다


t1 = (1, 2, 3)
t2 = tuple(t1)
print(t2 is t1)

t3 = t1[:]
print(t3 is t1)

print('=============')
t1 = (1,2,3,)
t3 = (1,2,3,)
print(t3 is t1)
s1 = 'ABC'  # 문자열에 대한 참조
s2 = 'ABC'  # 문자열에 대한 참조
print(s2 is s1)
