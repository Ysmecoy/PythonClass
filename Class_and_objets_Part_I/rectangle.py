class Rectangle:
    #constructor
    def __init__(self):
        self._width, self._height = 0,0
    # method
    def area(self):
        print( self._width*self._height)
r= Rectangle() #r is a object of Rectangle()
r._width, r._height = 3,5
print ("Area: %d" % r.area())
    
r_1, r_2 = Rectangle(), Rectangle()
r_1._width, r_1._height =2,10
r_2._width, r_2._height =3,5
print('Area: %.2f' % r_1.area())
print('Area: %.2f' % r_2.area())