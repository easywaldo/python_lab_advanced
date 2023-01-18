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