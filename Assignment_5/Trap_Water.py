def trap_water(heights):
    
    """ Calculate the units of water trapped.
        :param level: single list of integer  => list[int]
        :type level: int
        :returns: units of water trapped
        :rtype: int
    """
    list1 = [0,1,0,2,1,0,1,3,2,1,2,1]
    left, right = 0, len(heights)-1  # indicate the index of the left and right side of the list or elevation map
    left_wall, right_wall = 0, 0  # represent the value of water trapped in both extremes initially.
    unit_water = 0 # initialize the unit_water counter.
    
    # the method consists in check in both sides for the max level to reassign the max left side or right side or calculate the difference or unit of water
    while left < right:
        if heights[left] < heights[right]:
            if heights[left] < left_wall:
                left_wall = heights[left]
            else:
                unit_water += left_wall - heights[left]
                left += 1 # move the pointer to the next level or bar to the right
        else:
            if level[right] > right_wall:
                right_wall = level[right]
            else:
                unit_water += right_wall - level[right]
                right -= 1 # move the pointer to the next level or bar to the left
        return unit_water
   
    
    print(trap_water(list1))
# The main() program
'''
def main():
    # Open the input and output files.
    input_file = open("map.txt")
    output_file = open("result.txt", 'w')
    
    # Read the line from the input file.
    level = list(input_file)
    
    units_water = trap_water(level)
    output_file.write("%d\n" % units_water)
    
    # Close the files.
    input_file.close()
    output_file.close()


if __name__ == "__main__":
    main()
    '''