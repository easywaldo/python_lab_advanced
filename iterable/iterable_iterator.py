class Coll2:
    cc = 0
    def __init__(self,d):
        self.ds = d
    
    def __next__(self):
        if len(self.ds) <= self.cc:
            raise StopIteration
        self.cc += 1
        return self.ds[self.cc -1]
    
    def __iter__(self):
        self.cc = 0
        print('__iter__ called')
        return self
    
def main():
    co = Coll2([1,2,3,4,5,6,7,8,9,10])
    for i in co:
        print(i, end=' ')
    
    for i in co:
        print(i, end=' ')
        
    co = Coll2('HelloWorld')
    itr = iter(co)
    print(itr is co)


if __name__ == '__main__':
    main()
