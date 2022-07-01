
from math import sqrt

# Define the "distance()" function.

def distance(x1, y1, z1, x2, y2, z2):
    """ Calculates the distance between two points.
        :param x1,y1,z1: coordinate values of the first point.
        :type x1, y1, z1: float
        :param x2, y2, z2: coordinate values of the second point.
        :type x2, y2, z2: float
        :returns: distance between the two points 
        :rtype: float
    """
    distance_calc = sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
    return distance_calc
    

# The main() program

def main():
    # Open the input and output files.
    input_file = open("points.txt")
    output_file = open("result.txt", 'w')
    
    # Read all the lines in the input file.
    lines = input_file.readlines()
    
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
            dist_2_points = distance(x1, y1, z1, x2, y2, z2)
            output_file.write("%.2f\n"  % dist_2_points) # write the distance to the output file.  Each value is written in a separate line and have 2 decimal points.
    
    # Close the files.
    input_file.close()
    output_file.close()


if __name__ == "__main__":
    main()

