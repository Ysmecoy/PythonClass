class Rectangle(Shape):
    def __init__( self, x = 0.0, y = 0.0, width = 0, height = 0 ):
        """ Constructs a Rectangle object.
        :param x: x-coordinate value of the center of the rectangle
        :type x: float
        :param y: y-coordinate value of the center of the rectangle
        :type y: float
        :param width: width of the rectangle
        :type width: int
        :param height: height of the rectangle
        :type height: int
        :rtype: None
        """
        
        Shape.__init__(self, x, y)
        self._width = width
        self._height = height
        
    # Getters

    def get_width(self):
        """ Returns the width of the rectangle
            :returns: the width of the rectangle
            :rtype: int
        """
        return self._width

    def get_height(self):
        """ Returns the height of the rectangle
            :returns: the height of the rectangle
            :rtype: int
        """
        return self._height

    # Setters

    def set_width(self, width):
        """ Updates the width of the rectangle
            :param width: new value of the width of the rectangle
            :type width: int
            :rtype: None
        """
        self._width = width

    def set_height(self, height):
        """ Updates the height of the rectangle
            :param height: new value of the height of the rectangle
            :type y: int
            :rtype: None
        """
        self._height = height
        
    
       # Methods

    def area(self):
        """ Calculates the area of the rectangle.
            :returns: the area of the rectangle
            :rtype: float
        """
        area_rec = self._width*self._height
        return area_rec
      

    def perimeter(self):
        """ Calculates the perimeter of the rectangle.
            :returns: the perimeter of the rectangle
            :rtype: float
        """
        perimeter_rec = 2*(self._width + self._height)
        return perimeter_rec 
    
       
        
        
        