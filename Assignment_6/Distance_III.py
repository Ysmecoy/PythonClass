from math import sqrt

class Point:
    #constructor
    def __init__(self,x = 0.0, y = 0.0, z= 0.0 ):
        """ Constructs a point.
            :param _x: x-coordinate of the point
            :type _x: float
            :param _y: y-coordinate of the point
            :type _y: float
            :param _z: z-coordinate of the point
            :type _z: float
            :rtype: None
        """
        self._x = x
        self._y = y
        self._z = z
    
    #getters
    def get_x(self):
        """ Returns the x-coordinate x of the point.
            :returns: x-coordinate of the point
            :rtype: float
        """
        return self._x
        
    def get_y(self):
        """ Returns the y-coordinate of the point.
            :returns: y-coordinate of the point
            :rtype: float
        """
        return self._y
        
    def get_z(self):
        """ Returns the z-coordinate of the point.
            :returns: z-coordinate of the point
            :rtype: float
        """
        return self._z   
    #setters
    def set_x(self, x):
        """ Updates the x-coordinate of the point.
            :param x: updated value of x-coordinate of the point.
            :type x: float
            :rtype: None
        """
        self._x = x
        
    def set_y(self, y):
        """ Updates the y-coordinate y of the point.
            :param y: updated value of y-coordinate of the point.
            :type y: float
            :rtype: None
        """
        self._y = y
        
    def set_z(self, z):
        """ Updates the z-coordinate of the point.
            :param z: updated value of z-coordinate of the point.
            :type z: float
            :rtype: None
        """
        self._z = z
    
    #method
    def distance(self, other):
        """Calculates the distance between two points.
        :param other: another point of x,y,z coordinates values.
        :type other: float
        :returns: distance between the two points 
        :rtype: float
        """
        return sqrt((self._x - other._x)**2 + (self._y - other._y)**2 + (self._z - other._z)**2)
        
   

# The main() program

def main():
    # Open the input and output files.
    input_file = open("points.txt")
    output_file = open("result.txt", 'w')
    
    # Read all the lines in the input file.
    lines = input_file.readlines()
    print(lines[5])
    
    # Process each line.
    for line in lines:
        line = line.split()  # Split the values in the line by whitespaces.
        if len(line) == 6:  # Only process the line if it has 6 values (skip those empty lines).
            x1 = float(line[0]) # 6 values that represents the two points P1(x1,y1,z1) and P2(x2,y2,z2)  for each lines
            y1 = float(line[1])
            z1 = float(line[2])
            x2 = float(line[3])
            y2 = float(line[4])
            z2 = float(line[5])
            #create two objects or points type Point()
            p_1, p_2 = Point(x1, y1, z1), Point(x2, y2, z2)
            #calculate the distance between two points calling the method distance of the class Point
            distance_two_points = Point.distance(p_1,p_2)
            # write the distance to the output file.
            #Each value is written in a separate line and have 2 decimal points.
            output_file.write("%.2f\n"  % distance_two_points)   
    
    # Close the files.
    input_file.close()
    output_file.close()


if __name__ == "__main__":
    main()

