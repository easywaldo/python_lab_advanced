from dataclasses import dataclass


@dataclass
class C:
    a: int
    b: int  = 10
    
    # init is primary default value
    def __init__(self, a: int, b: int = 100):
        self.a = a
        self.b = b
        
c_data = C(a=1)
print(c_data)
    
    
        