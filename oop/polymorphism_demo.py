import math

class Shape:
    def __init__(self, length=None, width=None, radius=None):
        self.length = length
        self.width = width
        self.radius = radius
    
    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, length, width):
        # Only pass the length and width to the parent
        super().__init__(length=length, width=width)

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        # Only pass the radius to the parent
        super().__init__(radius=radius)
    
    def area(self):
        return math.pi * (self.radius * self.radius)
