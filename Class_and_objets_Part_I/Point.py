# The __init__ method constructor can be customized with additional parameters
class Point:
    def __init__(self, x_coord, y_coord, z_coord):
        self._x = x_coord
        self._y = y_coord
        self._z = z_coord
p_1, p_2 = Point(1,2,3), Point(4,5,6)
print('p_1: (%d, %d, %d)' % (p_1._x, p_1._y, p_1._z))
print('p_2: (%d, %d, %d)' % (p_2._x, p_2._y, p_2._z))

# parameters with default Values
class Point1:
    def __init__(self, X=0, Y=0, Z=0):
        self._x = X
        self._y = Y
        self._z = Z
p_3, p_4 = Point1(-1,3,4), Point1()
print('p_3: (%d, %d, %d)' % (p_3._x, p_3._y, p_3._z))
print('p_4: (%d, %d, %d)' % (p_4._x, p_4._y, p_4._z))

# defining a private string method:
class Point2:
    def __init__(self, X=0, Y=0, Z=0):
        self._x = X
        self._y = Y
        self._z = Z
    def __str__(self):
        s = '(' + str(self._x)+ ','
        s +=str(self._y) + ','
        s +=str(self._z) +')'
        return s
p_5 = Point2(10,20,30)
print(p_5)
