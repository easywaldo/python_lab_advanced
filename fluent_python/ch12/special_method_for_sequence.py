class MySeq:
    def __getitem__(self, index):
        return index
    
class Foo:
    def __iter__(self):
        pass
    


if __name__ == '__main__':
    s = MySeq()
    print(s[1])
    print(s[1:4])
    print(s[1:4:2])
    print(s[1:4:2, 9])
    print(s[1:4:2, 7:9])
    
    print(slice)
    print(dir(slice))
    
    s1 = slice(None, 10, 2).indices(5)
    s2 = slice(-3, None, None).indices(5)
    print(s1)
    print(s2)
    
    from collections import abc
    print(issubclass(Foo, abc.Iterable))
    f = Foo()
    print(isinstance(f, abc.Iterable))
    