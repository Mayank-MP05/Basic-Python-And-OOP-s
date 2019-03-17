import math
class Circle:
    def __init__(self,radius):
        self.r = radius

    def area(self):
        area = math.pi * self.r * self.r
        print(area)

c = Circle(7)
c.area()