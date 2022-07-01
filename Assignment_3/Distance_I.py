# Open input and output files.
from math import sqrt
input_file = open("points.txt")
output_file = open("result.txt", 'w')

# Read all lines in the input file.
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
        distance = sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2) # distance between two points
# write the distance to the output file.  Each value is written in a separate line and
# keep exactly 2 decimal places in the output values.
        output_file.write("%.2f\n" % distance)

# Close the files.
input_file.close()
output_file.close()
