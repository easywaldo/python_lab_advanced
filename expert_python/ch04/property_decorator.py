class Rectangle:
    def __init__(self, x1, x2, y1, y2):
        self.x1, self.y1 = x1, x2
        self.x2, self.y2 = y1, y2
    
    @property
    def width(self):
        return self.x2 - self.x1
    
    @width.setter
    def width(self, value):
        self.x2 = self.x1 + value
        
    @property
    def height(self):
        return self.y2 - self.y1
    
    @height.setter
    def height(self, value):
        self.y2 = self.y1 + value
        

rectangle_sample = Rectangle(10, 20, 10, 30)
print(rectangle_sample.height)
print(rectangle_sample.width)

rectangle_sample.width = 20
print(rectangle_sample.width)
rectangle_sample.height = 100
print(rectangle_sample.height)