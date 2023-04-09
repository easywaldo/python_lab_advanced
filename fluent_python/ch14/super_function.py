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