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