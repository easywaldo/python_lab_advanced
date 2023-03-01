from dataclasses import dataclass, field


@dataclass
class C:
    x: int
    y: int = field(repr=False)
    z: int = field(repr=True, default=10)
    t: int = 20
    
    # init is primary default value
    def __init__(self, x: int = 10, y: int = 10, z: int = 10, t: int = 100):
        self.x = x
        self.y = y
        self.z = z
        self.t = t
        
c_data = C()
print(c_data)
    
    
        