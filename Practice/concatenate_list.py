
'''
def concatenate(L1, L2):
    L1.extend(L2)
    L1 = L1 + L2
    return L2

list_1 = [2,6,5]
list_2 = [8,9,7]

print(concatenate(list_1, list_2))
'''

from math import pi, pow
class Shape:
    
    line_width = 1
    def __init__(self, x=0, y=0): self._x, self._y = x, y
    def get_location(self): return self._x, self._y
    def change_location(self, x, y): self._x, self._y = x, y
class Circle(Shape):
    def __init__(self, x=0, y=0, radius=0):
        Shape.__init__(self, x, y)
        self._radius = radius
    def area(self): return pi * pow(self._radius, 2)
    def circumference(self): return 2 * pi * self._radius
    
result = Shape.line_width
print(result)
