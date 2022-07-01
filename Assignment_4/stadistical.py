# Open input and output files.
from math import sqrt
input_file = open("input.txt")
output_file = open("output.txt", 'w')

# Read all lines in the input file.
lines = input_file.readlines()

# Process each line and built a list for x and y values
list_x = []
list_y = []
for line in lines:
    line = line.split()  # Split the values in the line by whitespaces.
    if len(line) == 2:  # Only process the line if it has 2 values ( x-y pairs) (skip those empty lines).
        xi = float(line[0]) # x-values
        list_x.append(xi) # append every x value to the list of xs.
        yi = float(line[1]) # y-values
        list_y.append(yi)
    
        
# 1)Number of x-y pairs in the input file
# find the numbers of lines or number of x-y pairs read in the input file

number_xy_pairs = len(open('input.txt').readlines(  ))


# 2)Average of x-values and average of y-values => total x or y values divided by the number of xy pairs

avg_xs = sum(list_x)/number_xy_pairs

avg_ys = sum(list_y)/number_xy_pairs


# 3)Standard deviation of x-values and standard deviation of y-values
# 3.1 Standard deviation of x- values 

sigma_x = 0 #initialize the sum of x-values

for xi in list_x:
    sigma_x += (xi - avg_xs)**2  # sum of each (xi - average of x values) by the power of 2
desv_stand_x = sqrt((sigma_x)/(number_xy_pairs))  # formula of standard deviation

     
#3.2 Standard deviation of y- values
sigma_y = 0 #initialize the sum of x-values

for yi in list_y:
    sigma_y += (yi - avg_ys)**2 # sum of each (yi - average of y values) by the power of 2
desv_stand_y = sqrt((sigma_y)/(number_xy_pairs))  # formula of standard deviation


# 4)Correlation coefficient of x-values and y-values
sigma_xy = 0 # initialize the sum of xy values
sum_of_dif = 0 # initialize the sum of difference 
for line in lines:
    line = line.split()  # Split the values in the line by whitespaces.
    if len(line) == 2:  # Only process the line if it has 2 values (skip those empty lines).
        xi = float(line[0])
        yi = float(line[1])
        sum_of_dif += (xi-avg_xs)*(yi - avg_ys) # according to the correlation coefficient formula, the numerator is the sum of difference of each point with respect to its average.
        sigma_xy += xi*yi



correlation_coefficient = ((sum_of_dif))/((sqrt(sigma_x))*(sqrt(sigma_y))) # formula of correlation coefficient


#5)Slope m and intercept b in the best-fitting line, y = mx + b, of x-values and y-values.

sum_of_x2 = 0
for xi in list_x: 
    sum_of_x2 += xi**2 
 
# slope = m in the best-fitting line, y = mx + b
slope = (number_xy_pairs*(sigma_xy) - (sum(list_x) * sum(list_y)))/((number_xy_pairs*(sum_of_x2))-(sum(list_x))**2) # formula of m


#b intercept is b in the best-fitting line, y = mx + b

intercept = ((sum(list_y) - slope*(sum(list_x)))/(number_xy_pairs)) # formula of b


output_file.write('Number of x-y pairs read: {} \n' .format(number_xy_pairs))
output_file.write('\n Algebraic average of x: {:.6f} \n Algebraic average of y: {:.6f} \n Standard deviation of x: {:.6f} \n Standard deviation of y: {:.6f} \n' .format(avg_xs, avg_ys, desv_stand_x, desv_stand_y))    
output_file.write('\n Correlation coefficient: {:.6f} \n'.format(correlation_coefficient))
output_file.write('\n Linear fitting function: \n')
output_file.write('\n y = {:.6f}x + {:.6f} \n' .format(slope,intercept)) # The least square best-fit straight line associated with n points
output_file.write('\n Slope: {:.6f} \n Intercept: {:.6f}' .format(slope,intercept))


# Close the files.
input_file.close()
output_file.close()