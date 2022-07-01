def trap_water(heights):
    """ Calculate the units of water trapped.
        :param heights: single list of integer  => list[int]
        :type heights: int
        :returns: units of water trapped
        :rtype: int
    """
    ''' algorithm: 1. Build lists called left and right of size = len(heights) where left[i] and right[i] represents the
        the maximun heights bars iterating from the left and from the right side respectively.
        2. initialize the sum of unit of water trapped = 0
        3. calculate the unit of water  iterating and regarding the min(left[i], right[i]) - height[i]
        return unit_water_trapped
        '''
    size=len(heights)
    left =size*[0] # Initialize empty list of given length
    right = size*[0]
    
    
    max_so_far_left=heights[0] # initialize the first element of the li as the maximun so far found.
    for index in range(0, size): # iterate from the item 0 in the li until the last one to create the left list of maximun heights.
        if(max_so_far_left < heights[index]):
            max_so_far_left=heights[index]
            left[index]=max_so_far_left
        else:
            left[index] = max_so_far_left # if the element to the left is less than the max_so_far_left founf; then, keep the max_so_far_left

    max_so_far_right = heights[-1] # initialize the max_so_far_right with the last element of the li
    for index in range(size-1, -1, -1): # iterate from right to left
        if(max_so_far_right < heights[index]):
            max_so_far_right = heights[index]
            right[index]=max_so_far_right
        else:
            right[index] = max_so_far_right

    unit_water_trapped = 0
    for index in range(0,size): # iterate regarding the lists, left and right, that contain the maximun levels or heights from side to side.
        unit_water_trapped = unit_water_trapped + min(left[index],right[index])-heights[index] # find the minimun between both list in the same index and rest the amount in the main or original list in the same index
    return unit_water_trapped


def main():
    # Open the input and output files.
    input_file = open("map.txt")
    output_file = open("result.txt", 'w')
    
    # Read the line or list from the input file.
    heights = input_file.read()
    heights = heights.split()
    heights = [int(i) for i in heights]

    units_water_calc = trap_water(heights)
    output_file.write("%d\n" % units_water_calc)
    
    # Close the files.
    input_file.close()
    output_file.close()


if __name__ == "__main__":
    main()