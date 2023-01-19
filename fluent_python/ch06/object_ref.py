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