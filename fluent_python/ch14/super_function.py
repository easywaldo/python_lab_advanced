from collections import OrderedDict


class LastUpdatedOrderdDict(OrderedDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.move_to_end(key)
        
last_updated_ordered_dict = LastUpdatedOrderdDict({
    "python": "A",
    "java": "A",
})

last_updated_ordered_dict["java"] = "S"
print(last_updated_ordered_dict)

class DoppelDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)
        
dd = DoppelDict(one=1)
print(dd)

dd['two'] = 2
print(dd)

dd.update(three=3)
print(dd)


print('================================')
class AnswerDict(dict):
    def __getitem__(self, key):
        return 42
    
ad = AnswerDict(a = 'foo')
print(ad['a'])

d = {}
d.update(ad)

print(d['a'])

print(d)

print(d['a'])   # ignored AnswerDict.__getitem__.


print('================================')
import collections

class DoppelDict2(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)
    
dd = DoppelDict2(one=1)
print(dd)
dd['two'] = 2
print(dd)

dd.update(three=3)
print(dd)

class AnswerDict2(collections.UserDict):
    def __getitem__(self, key):
        return 42
    
ad = AnswerDict2(a='foo')
print(ad['a'])

d = {}
d.update(ad)
print(d['a'])
print(d)

