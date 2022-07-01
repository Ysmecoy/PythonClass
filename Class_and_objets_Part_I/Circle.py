import math
class Circle:
    def __init__(self):
        self._x, self._y, self._r = 0,0,0
    #method area
    def area(self):
        return math.pi*self._r*self._r
    #method circumference
    def circumference(self):
        return 2*math.pi*self._r
    # method move
    def move(self, new_x, new_y):
        self._x, self._y = new_x, new_y   
        
# create an object of the class Circle
c = Circle()
c.move(2,12)
c._r = 1

print('Center: %d, %d' % (c._x, c._y))
print('Radius: %d' % (c._r))
print('Circumference: %.2f' % c.circumference())
print('Area: %.2f' % c.area())

