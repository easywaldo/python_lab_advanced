"""
shallow & deep copy

객체의 복사 종류

가변 : list, set, dict

복사의 종류 : copy, shallow copy, deep copy

"""

# Ex1 - Copy

a_list = [1,2,3,[4,5,6],7,8,9]
b_list = a_list

print('Ex1 > ', id(a_list))
print('Ex1 > ', id(b_list))

b_list[2] = 100

print('Ex1 > ', a_list)
print('Ex1 > ', b_list)


b_list[3][2] = 300

print('Ex1 > ', a_list)
print('Ex1 > ', b_list)


# Ex2 - shallow copy

import copy

c_list = [1,2,3,[4,5,6],[7,8,9]]
d_list = copy.copy(c_list)

print('Ex2 > ', id(c_list))
print('Ex2 > ', id(d_list))

d_list[1] = 9000

print('Ex2 > ', c_list)
print('Ex2 > ', d_list)

d_list[3].append(10000)
d_list[4][1] = 999999

print('Ex2 > ', c_list)
print('Ex2 > ', d_list)


# Ex3 - deep copy

e_list = [1,2,3,[4,5,6],[7,8,9]]
f_list = copy.deepcopy(e_list)

print('Ex3 > ', id(e_list))
print('Ex3 > ', id(f_list))


e_list[3].append(10000)
e_list[4][1] = 999999

print('Ex3 > ', e_list)
print('Ex3 > ', f_list)