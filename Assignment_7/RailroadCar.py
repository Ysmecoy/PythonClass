from math import pi

class RailroadCar:
#constructor
    def __init__(self,length = 0.0):
        """ Construct a RaildroadCar object
            :param length: length of the railroad object
            :type length: float
            :rtype: None
    
        """
        self._length = length 
    
    # Getter
    def get_length(self):
        """ Returns the length of the railroad car object.
            :returns: the length value of the railroad car
            :rtype: float
        """
        return self._length


    # Setters

    def set_length(self, length):
        """ Updates the length value of the railroad car.
            :param length: new value of the length
            :type length: float
            :rtype: None
        """
        self._length = length
     
        
    #Method
    
    def Volume(self):
        """ Calculates the volume of the railroad car.
            :returns: the volume of the railroad car
            :rtype: float
        """
        # Enforces that all derived classes must override this method.
        raise NotImplementedError
    
    
class TankCar(RailroadCar):
    #constructor
    def __init__( self, length = 0.0, radius= 0.0 ):
        """ Constructs a Tank car object that is a cylinder-shaped railroad car.
        :param length: length of the tank car object
        :type length: float
        :param radius: the radius value of the cylinder-shaped railroad car
        :type radius: float
        :rtype: None
        """
        
        RailroadCar.__init__(self, length)
        self._radius = radius
        
    # Getter
    def get_radius(self):
        """ Returns the radius of the cylinder-shaped railroad car object (Tank car).
            :returns: the radius value of the tank car
            :rtype: float
        """
        return self._radius


    # Setters

    def set_radius(self, radius):
        """ Updates the radius value of the tank car.
            :param radius: new value of the radius
            :type radius: float
            :rtype: None
        """
        self._radius = radius
    
    
    #Method
    
    def Volume(self):
        """ Calculates the volume of the tank car.
            :returns: the volume of the tank car
            :rtype: float
        """
        
        return pi*self._radius**2*self._length
    
    
    
class BoxCar(RailroadCar):
    #constructor
    def __init__( self, length = 0.0, width = 0.0, height = 0.0):
        """ Constructs a Box car object that is a cuboid-shaped railroad car.
        :param length: length of the box car object
        :type length: float
        :param width: the width value of the box car
        :type width: float
        :param height: the height value of the box car
        :type height: float
        :rtype: None
        """
        
        RailroadCar.__init__(self, length)
        self._width = width 
        self._height = height
    
    
    
    # Getter
    def get_width(self):
        """ Returns the width of the cuboid-shaped railroad car object (Box car).
            :returns: the width value of the box car
            :rtype: float
        """
        return self._width
    
    def get_height(self):
        """ Returns the height of the cuboid-shaped railroad car object (Box car).
            :returns: the height value of the box car
            :rtype: float
        """
        return self._height

    # Setters

    def set_width(self, width):
        """ Updates the width value of the box car.
            :param width: new value of the width
            :type width: float
            :rtype: None
        """
        self._width = width
        
        
    def set_height(self, height):
        """ Updates the height value of the box car.
            :param height: new value of the height
            :type height: float
            :rtype: None
        """
        self._height = height 
        
    #Method
    
    def Volume(self):
        """ Calculates the volume of the box car.
            :returns: the volume of the box car
            :rtype: float
        """
       
        return self._length*self._width*self._height
    
    
    
class RefrigeratorCar(BoxCar):
    #constructor
    def __init__( self, length = 0.0, width = 0.0, height = 0.0, temperature = 0.0):
        """ Constructs a Refrigerator car object that is a cuboid-shaped railroad car with a temperature.
        :param length: length of the Refrigerator car object
        :type length: float
        :param width: the width value of the Refrigerator car
        :type width: float
        :param height: the height value of the Refrigerator car
        :type height: float
        :param temperature: temperature of the Refrigerator car
        :type temperature: float
        :rtype: None
        """
        
        BoxCar.__init__(self, length, width, height)
        self._temperature = temperature
        
    # Getter
    def get_temperature(self):
        """ Returns the temperature of the Refrigerator car object.
            :returns: the temperature value of the refrigerator car
            :rtype: float
        """
        return self._temperature

    # Setter

    def set_temperature(self, temperature):
        """ Updates the temperature value of the Refrigerator car.
            :param temperature: new value of the temperature
            :type temperature: float
            :rtype: None
        """
        self._temperature = temperature
   

# The main() function program

def main():
    # Open the input and output files.
    input_file = open("cars.txt")
    output_file = open("results.txt", 'w')
    # Read all the lines in the input file.
    lines = input_file.readlines()
    # Process each line.
    car = None # create a car Object
    for line in lines:
        line = line.split()
        if len(line) > 1:
            if line[0] == 'Tank':
                length = float(line[1])
                radius = float(line[2])
                car = TankCar(length,radius )
            if line[0] == 'Box':
                length = float(line[1])
                width = float(line[2])
                height = float(line[3])
                car = BoxCar(length, width, height)
            if line[0] == 'Refrigerator':
                length = float(line[1])
                width = float(line[2])
                height = float(line[3])
                temperature = float(line[4])
                car = RefrigeratorCar(length, width, height, temperature)
            if car != None:
                volume_calc = car.Volume()
                output_file.write("%.2f\n" % volume_calc)
                car = None
    
    # Close the files.
    input_file.close()
    output_file.close()


if __name__ == "__main__":
    main()    
    