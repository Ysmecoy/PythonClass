
class Vector:
    #constructor
    """
       :param a: x-component of vector p.
       :type a: float
       :param b: y-component of vector p.
       :type b: float
       :param c: z-component of vector p.
       :type c: float
       :return: None
    """
    def __init__(self, a = 0.0, b = 0.0, c = 0.0):
        self._a = a
        self._b = b
        self._c = c
    
    #getters
    def get_a(self):
        """ Returns a, the x-component of vector p.
            :returns: a, the x-component of vector p.
            :rtype: float
        """
        return self._a
        
    def get_b(self):
        """ Returns b, the y-component of vector p.
            :returns: b, the y-component of vector p.
            :rtype: float
        """
        return self._b
        
    def get_c(self):
        """ Returns c, the z-component of vector p.
            :returns: c, the z-component of vector p.
            :rtype: float
        """
        return self._c   
    #setters
    def set_a(self, a):
        """ Updates a, the x-component of vector p.
            :param a: updated value of a, the x-component of vector p.
            :type a: float
            :rtype: None
        """
        self._a = a
        
    def set_b(self, b):
        """ Updates b, the y-component of vector p.
            :param b: updated value of b, the y-component of vector p.
            :type b: float
            :rtype: None
        """
        self._b = b
        
    def set_c(self, c):
        """ Updates c, the z-component of vector p.
            :param c: updated value of c, the z-component of vector p.
            :type c: float
            :rtype: None
        """
        self._c = c
        
    #method overloaded operator
    #Arithmetic multiplication operator ('*')
    
    def __mul__(self,other):
        """Multiplies the vector or components of a vector with another vector or other components using ('*')
           :param other: another vector or components of x, y, z => a,b,c.
           :type other: Vector
           :returns: multiplication result
           :rtype: Vector
        """
        
        if isinstance(other, Vector): v_2 = other
        else: raise NotImplementedError
        result = self._a*v_2._a + self._b*v_2._b + self._c*v_2._c
        return result
    
def main():
    # Open the input and output files.
    input_file = open("vectors.txt")
    output_file = open("result.txt", 'w')
    
    # Read all the lines in the input file.
    lines = input_file.readlines()
    
    # Process each line.
    for line in lines:
        line = line.split()  # Split the values in the line by whitespaces.
        if len(line) == 6:  # Only process the line if it has 6 values (skip those empty lines).
            a1 = float(line[0]) # 6 values that represents the two vectors v_1 = Vector(a1,b1,c1) and v_2 = Vector(a2,b2,c2)  for each lines
            b1 = float(line[1])
            c1 = float(line[2])
            a2 = float(line[3])
            b2 = float(line[4])
            c2 = float(line[5])
            
            #create two instances or objects of Vector type
            v_1, v_2 = Vector(a1, b1, c1), Vector(a2, b2, c2)
           
            #calculate the dot product between two vectors
            dot_product_vectors = Vector.__mul__(v_1,v_2)
            #Each value is written in a separate line and have 2 decimal points.
            output_file.write("%.2f\n"  % dot_product_vectors)
            
    # Close the files.
    input_file.close()
    output_file.close()


if __name__ == "__main__":
    main()
    
    
        
        
        