# Open the input and output files.
input_file = open("population.txt")
output_file = open("result.txt", 'w')

# Read the 4 values in the input file one by one into a list.
values = input_file.readlines()

# Convert the strings to integers and float to manipulate the data

population_A = int(values[0])
population_B = int(values[1])
incr_rate_A = float(values[2])
incr_rate_B = float(values[3])

# Iterations until population A is grater or equal to population B.
years = 0 # each iteration represents a year
while (population_B >= population_A):   # the while loop iterate while the condition between parenthesis is true; that means, population_B >= population_A; then, when is false  and break the loop, population A will be bigger than B
    population_A += population_A * incr_rate_A #calculate the increasing in the population in each town depending on the number of iteration or years
    population_B += population_B * incr_rate_B
    years += 1
    

# Write in result or output file the numbers of years required to make population of town A grater or equal to population of town B in a new different line with rounded values for populations.
output_file.write( '\n Years: {}\n Population of Town A: {} \n Population of Town B: {}' .format(years, round(population_A), round(population_B))) 



# Close the files.
input_file.close()
output_file.close()