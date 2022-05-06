"""
Descriptor

1. 상황에 맞는 메서드 구현을 통한 개체지향 프로그래밍 구현
2. Property 와 달리 reuse(재사용) 가능
3. ORM Framework 사용
"""

# Ex1
# Descriptor 예제 1

import os

class DirectoryFileCount:
    def __get__(self, obj, objtype=None):
        # print(os.listdir(obj.dirname))
        return len(os.listdir(obj.dirname))
    
class DirectoryPath:
    size = DirectoryFileCount()
    
    def __init__(self, dirname):
        self.dirname = dirname
        
# 현재 경로
s = DirectoryPath('./')
print(s.size)

# 이전 경로
g = DirectoryPath('../')
print(g.size)

# 혼동이 되는 경우 출력 용도
print('Ex1 > ', dir(DirectoryPath))
print('Ex1 > ', DirectoryPath.__dict__)
print('Ex1 > ', dir(s))
print('Ex1 > ', s.__dict__)


# Ex2
# Descriptor 예제 2

import logging

logging.basicConfig(
    format='%(asctime)s %(message)s', 
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


class LoggedScoreAccess:
    def __init__(self, value=50):
        self.value = value

    def __get__(self, obj, objtype=None):
        logging.info('Accessing %r giving %r', 'score', self.value)
        return self.value
    
    def __set__(self, obj, value):
        logging.info('Updating %r giving %r', 'score', self.value)
        self.value = value

class Student:
    # Descriptor instance
    score = LoggedScoreAccess()
    
    def __init__(self, name):
        # Regular instance attribute
        self.name = name
        
s1 = Student('Gimmy')
s2 = Student('Waldo')

# 점수 확인
print('Ex2 > ', s1.score)
s1.score += 20

# 점수 재확인
print('Ex2 > ', s1.score)

s2.score += 30
print('Ex2 > ', s2.score)


# __dict__확인
print('Ex2 > ', vars(s1))
print('Ex2 > ', vars(s2))
print('Ex2 > ', s1.__dict__)
print('Ex2 > ', s2.__dict__)
