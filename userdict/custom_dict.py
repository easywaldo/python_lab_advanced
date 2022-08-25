class UpperCaseDict(dict):
    def __setitem__(self, key, value):
        key = key.upper()
        super().__setitem__(key, value)
        
numbers = UpperCaseDict()
numbers["one"] = 1
numbers["two"] = 2
numbers["three"] = 3

if __name__ == "__main__":
    print(numbers)