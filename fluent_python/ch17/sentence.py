import re
import reprlib
from typing import List


RE_WORD = re.compile(r'\w+')

class Sentence(object):
    
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
        
    def __getitem__(self, index):
        return self.words[index]
    
    def __len__(self):
        return len(self.words)
    
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
    
s = Sentence('" The time has come, ", the Walrus said,')
print(s)

for word in s:
    print(word)
    
print(list(s))

print(s[0])
print(s[5])
print(s[-1])


class Spam:
    
    def __init__(self, items: List):
        self.items = items
        
    def __getitem__(self, i):
        return self.items[i]
    
spam_can = Spam([1,2,3,4,5])
print(iter(spam_can))

print(list(spam_can))

from collections import abc
print(isinstance(spam_can, abc.Iterable))

spam = Spam([1,2,3,4,5])

item_iter = iter(spam_can)
for item in item_iter:
    print(item)
