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