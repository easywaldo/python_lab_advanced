from dataclasses import dataclass, field
import random

def random_value():
    return random.randint(1, 100)

@dataclass
class C:
    x: int
    y: int = field(repr=True, default_factory=random_value)
    z: int = field(repr=True, default=10)
    t: int = 20
    
    # # init is primary default value
    # def __init__(self, x: int, y: int, z: int = 10, t: int = 100):
    #     self.x = x
    #     self.y = y
    #     self.z = z
    #     self.t = t
        
        
c_data = C(x=10)
print(c_data)
